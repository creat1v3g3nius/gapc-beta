#!/usr/bin/env python3
"""Detect semantic noise patterns in markdown documentation.

This checker targets governance noise that is not always structural:
- lexical ID variants (GUARDRAILS vs GUARD_RAILS, COMPOSANT vs COMPOSANTS)
- path-like or ghost depends_on entries
- likely typo variants in depends_on
- semantically duplicate titles
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import unicodedata
from dataclasses import asdict, dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable
from frontmatter_utils import parse_frontmatter_file

SEVERITY_ORDER = {"P0": 0, "P1": 1, "P2": 2}
ID_RE = re.compile(r"^[A-Z0-9_]+$")
KEY_VALUE_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$")


@dataclass(frozen=True)
class Issue:
    severity: str
    file: str
    line: int
    rule: str
    message: str
    expected_fix: str


@dataclass
class ParsedDoc:
    path: Path
    rel_path: str
    metadata: dict[str, str]
    line_map: dict[str, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check semantic noise in markdown documents.")
    parser.add_argument("--repo-root", default=".", help="Repo root path (default: current directory)")
    parser.add_argument("--scope", default="vault", help="Scope root to analyze (default: vault)")
    parser.add_argument(
        "--glob",
        action="append",
        default=["*.md"],
        help="Glob pattern inside scope (repeatable, default: *.md)",
    )
    parser.add_argument(
        "--output",
        choices=("text", "json"),
        default="text",
        help="Output mode",
    )
    parser.add_argument(
        "--min-severity",
        choices=("P0", "P1", "P2"),
        default="P2",
        help="Minimum severity to display",
    )
    parser.add_argument(
        "--report",
        help="Optional report output file. In json mode writes JSON; in text mode writes text output.",
    )
    parser.add_argument(
        "--max-suggestions",
        type=int,
        default=3,
        help="Maximum number of candidate IDs suggested for typo-like depends_on entries.",
    )
    return parser.parse_args()


def _line_for(line_map: dict[str, int], key: str) -> int:
    return line_map.get(key, 1)


def collect_markdown_files(scope_root: Path, patterns: Iterable[str]) -> list[Path]:
    files: set[Path] = set()
    for pattern in patterns:
        for path in scope_root.rglob(pattern):
            if path.is_file() and path.suffix == ".md":
                files.add(path.resolve())
    return sorted(files)


def parse_frontmatter(path: Path, repo_root: Path) -> tuple[ParsedDoc | None, list[Issue]]:
    rel_path = str(path.relative_to(repo_root))
    result = parse_frontmatter_file(path, KEY_VALUE_RE)
    if result.error_code == "missing_opening":
        return None, [
            Issue(
                severity="P0",
                file=rel_path,
                line=result.error_line or 1,
                rule="frontmatter_present",
                message=result.error_message or "frontmatter missing (expected opening ---)",
                expected_fix="add YAML frontmatter with required keys",
            )
        ]
    if result.error_code == "missing_closing":
        return None, [
            Issue(
                severity="P0",
                file=rel_path,
                line=result.error_line or 1,
                rule="frontmatter_closed",
                message=result.error_message or "frontmatter missing closing ---",
                expected_fix="close YAML frontmatter with ---",
            )
        ]
    return ParsedDoc(
        path=path,
        rel_path=rel_path,
        metadata=result.metadata,
        line_map=result.line_map,
    ), []


def parse_depends_list(raw: str) -> list[str] | None:
    value = raw.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return None
    inner = value[1:-1].strip()
    if not inner:
        return []
    return [chunk.strip() for chunk in inner.split(",") if chunk.strip()]


def split_camel_case(value: str) -> list[str]:
    expanded = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", value)
    return [tok for tok in re.split(r"[^A-Za-z0-9]+", expanded) if tok]


def stem_token(token: str) -> str:
    normalized = unicodedata.normalize("NFKD", token).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^a-z0-9]", "", normalized.lower())
    if not value:
        return ""
    if value.endswith("ies") and len(value) > 4:
        value = value[:-3] + "y"
    elif value.endswith("es") and len(value) > 4:
        value = value[:-2]
    elif value.endswith("s") and len(value) > 4:
        value = value[:-1]
    return value


def semantic_key_from_tokens(tokens: list[str]) -> str:
    stems = [stem_token(t) for t in tokens]
    return "_".join([s for s in stems if s])


def id_content_tokens(doc_id: str) -> list[str]:
    parts = [p for p in doc_id.split("_") if p]
    if len(parts) >= 2 and parts[1].isdigit():
        parts = parts[2:]
    elif len(parts) >= 1:
        parts = parts[1:]
    return parts


def id_content_signature(doc_id: str) -> str:
    return "_".join(id_content_tokens(doc_id))


def semantic_key_for_id(doc_id: str) -> str:
    tokens = id_content_tokens(doc_id)
    if not tokens:
        tokens = [doc_id]
    return semantic_key_from_tokens(tokens)


def suggest_similar_ids(
    dep_id: str,
    known_ids: list[str],
    id_semantic_keys: dict[str, str],
    limit: int,
) -> list[str]:
    dep_key = semantic_key_for_id(dep_id)
    scored: list[tuple[float, str]] = []
    for known in known_ids:
        known_key = id_semantic_keys[known]
        ratio = SequenceMatcher(None, dep_key, known_key).ratio()
        if ratio >= 0.82:
            scored.append((ratio, known))
    scored.sort(key=lambda pair: (-pair[0], pair[1]))

    suggestions: list[str] = []
    for _, candidate in scored:
        if candidate == dep_id:
            continue
        if candidate not in suggestions:
            suggestions.append(candidate)
        if len(suggestions) >= limit:
            break
    return suggestions


def detect_status(counts: dict[str, int]) -> str:
    if counts["P0"] > 0:
        return "FAIL"
    if counts["P1"] > 0:
        return "WARN"
    return "PASS"


def exit_code_for(status: str) -> int:
    if status == "FAIL":
        return 1
    if status == "WARN":
        return 2
    return 0


def add_issue(
    issues: list[Issue],
    severity: str,
    doc: ParsedDoc,
    line: int,
    rule: str,
    message: str,
    expected_fix: str,
) -> None:
    issues.append(
        Issue(
            severity=severity,
            file=doc.rel_path,
            line=line,
            rule=rule,
            message=message,
            expected_fix=expected_fix,
        )
    )


def collect_repo_ids(repo_root: Path) -> set[str]:
    vault_root = repo_root / "vault"
    if not vault_root.exists():
        return set()

    repo_ids: set[str] = set()
    for path in vault_root.rglob("*.md"):
        result = parse_frontmatter_file(path, KEY_VALUE_RE)
        if result.error_code is not None:
            continue
        doc_id = result.metadata.get("id", "").strip()
        if doc_id:
            repo_ids.add(doc_id)

    return repo_ids


def run_checker(args: argparse.Namespace) -> tuple[int, str]:
    repo_root = Path(args.repo_root).resolve()
    scope_root = (repo_root / args.scope).resolve()
    if not scope_root.exists():
        text = f"FAIL scope does not exist: {scope_root}\n"
        return 1, text

    files = collect_markdown_files(scope_root, args.glob)
    parsed_docs: list[ParsedDoc] = []
    issues: list[Issue] = []

    for path in files:
        parsed, parse_errors = parse_frontmatter(path, repo_root)
        issues.extend(parse_errors)
        if parsed is not None:
            parsed_docs.append(parsed)

    id_index: dict[str, list[ParsedDoc]] = {}
    for doc in parsed_docs:
        doc_id = doc.metadata.get("id", "").strip()
        if not doc_id:
            add_issue(
                issues,
                "P0",
                doc,
                _line_for(doc.line_map, "id"),
                "required_id",
                "missing required key: id",
                "set id in frontmatter",
            )
            continue
        if not ID_RE.match(doc_id):
            add_issue(
                issues,
                "P1",
                doc,
                _line_for(doc.line_map, "id"),
                "id_naming",
                "id should follow [A-Z0-9_]+",
                "normalize ID naming",
            )
        id_index.setdefault(doc_id, []).append(doc)

    for doc_id, docs in id_index.items():
        if len(docs) <= 1:
            continue
        for doc in docs:
            add_issue(
                issues,
                "P0",
                doc,
                _line_for(doc.line_map, "id"),
                "id_unique",
                f"duplicate id detected: {doc_id}",
                "keep one unique ID per file across scope",
            )

    repo_ids = collect_repo_ids(repo_root)
    known_ids = sorted(repo_ids or set(id_index.keys()))
    id_semantic_keys = {doc_id: semantic_key_for_id(doc_id) for doc_id in known_ids}

    # Depends_on semantic and structural checks.
    for doc in parsed_docs:
        raw_depends = doc.metadata.get("depends_on", "").strip()
        if not raw_depends:
            continue
        deps = parse_depends_list(raw_depends)
        if deps is None:
            add_issue(
                issues,
                "P0",
                doc,
                _line_for(doc.line_map, "depends_on"),
                "depends_format",
                "depends_on must be a YAML-like inline list: [ID1, ID2]",
                "rewrite depends_on as an ID list",
            )
            continue

        for dep in deps:
            if "/" in dep or dep.endswith(".md") or dep.startswith("vault"):
                add_issue(
                    issues,
                    "P0",
                    doc,
                    _line_for(doc.line_map, "depends_on"),
                    "depends_paths",
                    f"depends_on must reference IDs only, got path-like value: {dep}",
                    "replace path with canonical document ID",
                )
                continue

            if dep in repo_ids or dep in id_index:
                continue

            suggestions = suggest_similar_ids(dep, known_ids, id_semantic_keys, args.max_suggestions)
            if suggestions:
                add_issue(
                    issues,
                    "P1",
                    doc,
                    _line_for(doc.line_map, "depends_on"),
                    "depends_variant",
                    f"depends_on unknown ID '{dep}', close matches: {', '.join(suggestions)}",
                    "use canonical ID spelling in depends_on",
                )
            else:
                add_issue(
                    issues,
                    "P0",
                    doc,
                    _line_for(doc.line_map, "depends_on"),
                    "depends_ghost",
                    f"depends_on references unknown ID: {dep}",
                    "fix typo or create missing target document",
                )

    # ID lexical variant groups (same semantic key, different canonical IDs).
    semantic_id_index: dict[str, list[str]] = {}
    for doc_id in known_ids:
        key = id_semantic_keys[doc_id]
        if key:
            semantic_id_index.setdefault(key, []).append(doc_id)

    id_signature = {doc_id: id_content_signature(doc_id) for doc_id in known_ids}
    for key, ids in semantic_id_index.items():
        unique_ids = sorted(set(ids))
        if len(unique_ids) <= 1:
            continue
        signatures = {id_signature[i] for i in unique_ids}
        # Same concept replicated across families (same exact content signature)
        # is expected in this vault and should not be reported as semantic noise.
        if len(signatures) <= 1:
            continue
        for doc_id in unique_ids:
            for doc in id_index.get(doc_id, []):
                peers = [
                    i
                    for i in unique_ids
                    if i != doc_id and id_signature[i] != id_signature[doc_id]
                ]
                if not peers:
                    continue
                add_issue(
                    issues,
                    "P1",
                    doc,
                    _line_for(doc.line_map, "id"),
                    "id_semantic_variant",
                    f"ID semantic variant group '{key}' also contains: {', '.join(peers[:3])}",
                    "normalize to one canonical naming form and update references",
                )

    # Semantic title duplicates (normalized token set).
    title_key_index: dict[str, list[ParsedDoc]] = {}
    for doc in parsed_docs:
        title = doc.metadata.get("title", "").strip()
        if not title:
            continue
        title_key = semantic_key_from_tokens(split_camel_case(title))
        if title_key:
            title_key_index.setdefault(title_key, []).append(doc)

    for key, docs in title_key_index.items():
        ids = sorted({d.metadata.get("id", "").strip() for d in docs if d.metadata.get("id", "").strip()})
        if len(ids) <= 1:
            continue
        for doc in docs:
            doc_id = doc.metadata.get("id", "").strip()
            others = [i for i in ids if i != doc_id]
            if not others:
                continue
            add_issue(
                issues,
                "P2",
                doc,
                _line_for(doc.line_map, "title"),
                "title_semantic_duplicate",
                f"title semantics overlap with other IDs: {', '.join(others[:3])}",
                "keep one canonical title semantics per concept",
            )

    issues.sort(key=lambda i: (SEVERITY_ORDER[i.severity], i.file, i.line, i.rule))

    counts = {"P0": 0, "P1": 0, "P2": 0}
    for issue in issues:
        counts[issue.severity] += 1

    status = detect_status(counts)
    min_level = SEVERITY_ORDER[args.min_severity]
    display_issues = [i for i in issues if SEVERITY_ORDER[i.severity] <= min_level]

    report = {
        "status": status,
        "scope": str(scope_root),
        "files_scanned": len(files),
        "counts": counts,
        "issues": [asdict(issue) for issue in issues],
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    }

    if args.output == "json":
        output_text = json.dumps(report, ensure_ascii=True, indent=2) + "\n"
    else:
        lines: list[str] = []
        lines.append(f"SemanticNoiseChecker {status}")
        lines.append(f"scope: {scope_root}")
        lines.append(f"files_scanned: {len(files)}")
        lines.append(f"counts: P0={counts['P0']} P1={counts['P1']} P2={counts['P2']}")
        if display_issues:
            lines.append("issues:")
            for issue in display_issues:
                lines.append(
                    f"- {issue.severity} {issue.file}:{issue.line} [{issue.rule}] {issue.message} | fix: {issue.expected_fix}"
                )
        else:
            lines.append("issues: none at selected severity")
        output_text = "\n".join(lines) + "\n"

    if args.report:
        Path(args.report).write_text(output_text, encoding="utf-8")

    return exit_code_for(status), output_text


def main() -> int:
    args = parse_args()
    code, output_text = run_checker(args)
    sys.stdout.write(output_text)
    return code


if __name__ == "__main__":
    sys.exit(main())
