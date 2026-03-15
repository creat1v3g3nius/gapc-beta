#!/usr/bin/env python3
"""Check transverse document integrity across a markdown scope.

DocIntegrityChecker focuses on transverse consistency:
- id == filename
- id uniqueness
- depends_on validity and ghost references
- naming harmony checks (title/type/prefix/scope coherence)
- editorial governance checks (H1, changelog, FROZEN amendment section)
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable
from frontmatter_utils import parse_frontmatter_file

SEVERITY_ORDER = {"P0": 0, "P1": 1, "P2": 2}
VALID_ARCS = {"SYSTEM", "CORE", "PACKAGE", "PRODUCT", "CACHE"}
ARC_BY_FOLDER = {
    "00_SYSTEM": "SYSTEM",
    "01_CORE": "CORE",
    "02_PACKAGE": "PACKAGE",
    "03_PRODUCT": "PRODUCT",
    "99_CACHE": "CACHE",
    "04_CACHE": "CACHE",
}

ID_RE = re.compile(r"^[A-Z0-9_]+$")
TITLE_RE = re.compile(r"^[A-Z][A-Za-z0-9]*$")
KEY_VALUE_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$")
INDEX_DIR_RE = re.compile(r"^(?P<prefix>[A-Z0-9]+)_00_INDEX$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
CHANGELOG_ENTRY_RE = re.compile(r"^- v(?P<version>\d+\.\d+) \((?P<date>\d{2}-\d{2}-\d{4})\)")

# Allowed ID prefixes by frontmatter type for harmony checks.
# This avoids over-flagging package-specific families (GAPC_*, ASSO_*, HOSTING_*).
ALLOWED_PREFIXES_BY_TYPE = {
    "RUN": {"RUN"},
    "GIT": {"GIT"},
    "INDEX": {"INDEX", "CORE", "GAPC", "ASSO", "CACHE"},
    "META": {"META", "GAPC", "ASSO"},
    "DISCIPLINE": {"DISCIPLINE", "GAPC", "ASSO"},
    "CONSTRAINT": {"CONSTRAINT", "GAPC", "ASSO"},
    "PATCH": {"PATCH", "HOSTING", "FRAMEWORK"},
    "SCRIPT": {"SCRIPT"},
    "SCRIPTS": {"SCRIPT"},
    "LLM": {"LLM"},
    "FAQ": {"FAQ"},
    "BACKLOG": {"BACKLOG"},
    "EVIDENCE": {"EVIDENCE"},
    # PRODUCT may carry hybrid OPS_* files typed as DOD for gate/checklist controls.
    "DOD": {"DOD", "OPS"},
    "PRD": {"OPS"},
    "SPEC": {"OPS"},
    "ACTION": {"OPS"},
    "BACKLOG_CO": {"OPS"},
    "TOOLING": {
        "PIPELINE",
        "TPL",
        "EXTENSION",
        "KNOWLEDGE",
        "CHECKLIST",
        "GAPC",
        "ASSO",
    },
}

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
    re.compile(r"(?i)\b(api[_-]?key|token|secret|password)\b\s*[:=]\s*\S+"),
]


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
    frontmatter_raw: str
    text: str


@dataclass(frozen=True)
class Heading:
    line: int
    level: int
    text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check transverse doc integrity in markdown files.")
    parser.add_argument("--repo-root", default=".", help="Repo root path (default: current directory)")
    parser.add_argument("--scope", default="vault", help="Scope root to analyze (default: vault)")
    parser.add_argument(
        "--glob",
        action="append",
        default=["*.md"],
        help="Glob pattern inside scope (repeatable, default: *.md)",
    )
    parser.add_argument(
        "--file",
        action="append",
        default=[],
        help="Specific file relative to repo root (repeatable).",
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
        "--allow-id",
        action="append",
        default=[],
        help="Allow unresolved depends_on ID (repeatable)",
    )
    parser.add_argument(
        "--allowlist-file",
        help="File containing one allowed unresolved ID per line",
    )
    parser.add_argument(
        "--report",
        help="Optional report output file. In json mode writes JSON; in text mode writes text output.",
    )
    return parser.parse_args()


def load_allowlist(path: str | None) -> set[str]:
    if not path:
        return set()
    allowlist_path = Path(path)
    if not allowlist_path.exists():
        return set()
    ids: set[str] = set()
    for raw in allowlist_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        ids.add(line)
    return ids


def _line_for(line_map: dict[str, int], key: str) -> int:
    return line_map.get(key, 1)


def parse_frontmatter(path: Path, repo_root: Path) -> tuple[ParsedDoc | None, list[Issue]]:
    rel_path = str(path.relative_to(repo_root))
    text = path.read_text(encoding="utf-8", errors="replace")
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

    parsed = ParsedDoc(
        path=path,
        rel_path=rel_path,
        metadata=result.metadata,
        line_map=result.line_map,
        frontmatter_raw=result.raw,
        text=text,
    )
    return parsed, []


def collect_markdown_files(repo_root: Path, scope: Path, patterns: Iterable[str], explicit: list[str]) -> list[Path]:
    files: set[Path] = set()
    if explicit:
        for rel in explicit:
            p = (repo_root / rel).resolve()
            if p.exists() and p.is_file() and p.suffix == ".md":
                files.add(p)
    else:
        for pattern in patterns:
            for path in scope.rglob(pattern):
                if path.is_file() and path.suffix == ".md":
                    files.add(path.resolve())
    return sorted(files)


def parse_depends_list(raw: str) -> list[str] | None:
    value = raw.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return None
    inner = value[1:-1].strip()
    if not inner:
        return []
    return [chunk.strip() for chunk in inner.split(",") if chunk.strip()]


def expected_index_prefix_for_doc(doc: ParsedDoc) -> str | None:
    parent_name = doc.path.parent.name
    match = INDEX_DIR_RE.match(parent_name)
    if not match:
        return None
    prefix = match.group("prefix")
    if prefix in {"SYSTEM", "CORE"}:
        return "INDEX_"
    return f"{prefix}_INDEX_"


def expected_h1_prefix(doc_id: str) -> str | None:
    parts = [part for part in doc_id.split("_") if part]
    prefix_parts: list[str] = []
    for part in parts:
        prefix_parts.append(part)
        if part.isdigit():
            return "_".join(prefix_parts)
    return None


def parse_headings(text: str) -> list[Heading]:
    headings: list[Heading] = []
    in_code_fence = False

    for line_no, raw_line in enumerate(text.splitlines(), start=1):
        stripped = raw_line.rstrip()
        if stripped.startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue
        match = HEADING_RE.match(stripped)
        if not match:
            continue
        headings.append(Heading(line=line_no, level=len(match.group(1)), text=match.group(2).strip()))

    return headings


def find_first_changelog_entry(text: str, headings: list[Heading]) -> tuple[int, str, str] | None:
    changelog_heading: Heading | None = None
    changelog_index = -1
    for idx, heading in enumerate(headings):
        if heading.text == "Changelog":
            changelog_heading = heading
            changelog_index = idx

    if changelog_heading is None:
        return None

    lines = text.splitlines()
    end_line = len(lines) + 1
    for heading in headings[changelog_index + 1 :]:
        if heading.level <= changelog_heading.level:
            end_line = heading.line
            break

    for line_no in range(changelog_heading.line + 1, end_line):
        match = CHANGELOG_ENTRY_RE.match(lines[line_no - 1].strip())
        if match:
            return line_no, f"v{match.group('version')}", match.group("date")

    return None


def in_scope(path: Path, scope_root: Path) -> bool:
    try:
        path.relative_to(scope_root)
        return True
    except ValueError:
        return False


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

    allowlist_ids = set(args.allow_id)
    allowlist_ids |= load_allowlist(args.allowlist_file)
    repo_ids = collect_repo_ids(repo_root)

    files = collect_markdown_files(repo_root, scope_root, args.glob, args.file)
    parsed_docs: list[ParsedDoc] = []
    issues: list[Issue] = []

    # Step 1 & 2: collect and parse frontmatter.
    for path in files:
        parsed, parse_errors = parse_frontmatter(path, repo_root)
        issues.extend(parse_errors)
        if parsed is not None:
            parsed_docs.append(parsed)

    # Required metadata checks + obvious P0 checks.
    required_keys = ("id", "type", "title", "depends_on", "arc", "scope")
    for doc in parsed_docs:
        for key in required_keys:
            if not doc.metadata.get(key, "").strip():
                add_issue(
                    issues,
                    "P0",
                    doc,
                    _line_for(doc.line_map, key),
                    "required_key",
                    f"missing required key: {key}",
                    f"set `{key}` in frontmatter",
                )

        # Secret/PII heuristics in frontmatter.
        for pattern in SECRET_PATTERNS:
            if pattern.search(doc.frontmatter_raw):
                add_issue(
                    issues,
                    "P0",
                    doc,
                    1,
                    "secrets_policy",
                    "potential secret/token detected in frontmatter",
                    "remove secret-like values from metadata",
                )
                break

        doc_id = doc.metadata.get("id", "").strip()
        if doc_id and doc_id != doc.path.stem:
            add_issue(
                issues,
                "P0",
                doc,
                _line_for(doc.line_map, "id"),
                "id_filename",
                f"id must match filename stem (id={doc_id}, file={doc.path.stem})",
                "rename file or update id so both match",
            )

        if doc_id and not ID_RE.match(doc_id):
            add_issue(
                issues,
                "P1",
                doc,
                _line_for(doc.line_map, "id"),
                "id_naming",
                "id should follow [A-Z0-9_]+",
                "normalize id naming to uppercase snake style",
            )

        title = doc.metadata.get("title", "").strip()
        if title and not TITLE_RE.match(title):
            add_issue(
                issues,
                "P1",
                doc,
                _line_for(doc.line_map, "title"),
                "title_naming",
                "title should be UpperCamelCase",
                "normalize title casing",
            )

        arc = doc.metadata.get("arc", "").strip()
        if arc and arc not in VALID_ARCS:
            add_issue(
                issues,
                "P0",
                doc,
                _line_for(doc.line_map, "arc"),
                "arc_value",
                f"invalid arc: {arc}",
                f"use one of: {', '.join(sorted(VALID_ARCS))}",
            )

        scope = doc.metadata.get("scope", "").strip()
        if scope and not scope.startswith("vault/"):
            add_issue(
                issues,
                "P0",
                doc,
                _line_for(doc.line_map, "scope"),
                "scope_format",
                "scope must start with vault/",
                "set scope to a vault/... path",
            )

        # P1 harmony: arc/scope coherence.
        if arc and scope.startswith("vault/"):
            parts = scope.split("/")
            if len(parts) > 1:
                inferred_arc = ARC_BY_FOLDER.get(parts[1])
                if inferred_arc and inferred_arc != arc:
                    add_issue(
                        issues,
                        "P1",
                        doc,
                        _line_for(doc.line_map, "scope"),
                        "arc_scope_harmony",
                        f"scope folder suggests arc={inferred_arc} but arc={arc}",
                        "align arc and scope folder",
                    )

        # P1 harmony: type/prefix coherence when mapping exists.
        doc_type = doc.metadata.get("type", "").strip()
        prefix = doc.metadata.get("id", "").strip().split("_", 1)[0] if doc.metadata.get("id") else ""
        allowed_prefixes = ALLOWED_PREFIXES_BY_TYPE.get(doc_type)
        if allowed_prefixes and prefix and prefix not in allowed_prefixes:
            add_issue(
                issues,
                "P1",
                doc,
                _line_for(doc.line_map, "type"),
                "type_prefix_harmony",
                f"type {doc_type} expects one of {sorted(allowed_prefixes)} prefixes, got {prefix}_*",
                "align type and ID family or expand checker policy if this family is valid",
            )

        expected_index_prefix = expected_index_prefix_for_doc(doc)
        if doc_type == "INDEX" and expected_index_prefix and doc_id and not doc_id.startswith(
            expected_index_prefix
        ):
            add_issue(
                issues,
                "P1",
                doc,
                _line_for(doc.line_map, "id"),
                "index_family_naming",
                "index file should use canonical family prefix "
                f"{expected_index_prefix}NUM_TITRE, got {doc_id}",
                f"rename file/id to start with {expected_index_prefix}",
            )

        # P1 harmony: scope should include file path parent.
        if scope.startswith("vault/"):
            scope_path = (repo_root / scope).resolve()
            if scope_path.exists() and scope_path.is_dir() and not in_scope(doc.path.resolve(), scope_path):
                add_issue(
                    issues,
                    "P1",
                    doc,
                    _line_for(doc.line_map, "scope"),
                    "scope_path_harmony",
                    "file is outside declared scope directory",
                    "align scope with actual file directory",
                )

        headings = parse_headings(doc.text)
        h1_headings = [heading for heading in headings if heading.level == 1]
        if len(h1_headings) != 1:
            add_issue(
                issues,
                "P0",
                doc,
                h1_headings[0].line if h1_headings else 1,
                "h1_unique",
                f"document must contain exactly one H1, found {len(h1_headings)}",
                "keep a single H1 in the markdown body",
            )
        elif doc_id:
            expected_prefix = expected_h1_prefix(doc_id)
            h1_text = h1_headings[0].text
            if expected_prefix and not (
                h1_text.startswith(f"{expected_prefix} - ")
                or h1_text.startswith(f"{expected_prefix} — ")
            ):
                add_issue(
                    issues,
                    "P1",
                    doc,
                    h1_headings[0].line,
                    "h1_naming",
                    f"H1 should start with `{expected_prefix} - `, got `{h1_text}`",
                    f"rename H1 to start with `{expected_prefix} - `",
                )

        status = doc.metadata.get("status", "").strip()
        if status == "FROZEN":
            amend_heading = next(
                (heading for heading in headings if heading.text == "Amendements (FROZEN)"),
                None,
            )
            if amend_heading is None:
                add_issue(
                    issues,
                    "P0",
                    doc,
                    1,
                    "frozen_amendments_section",
                    "FROZEN document must include `## Amendements (FROZEN)`",
                    "add the controlled amendment section for FROZEN documents",
                )

            changelog_heading = next((heading for heading in headings if heading.text == "Changelog"), None)
            if changelog_heading is None:
                add_issue(
                    issues,
                    "P1",
                    doc,
                    1,
                    "frozen_changelog_section",
                    "FROZEN document should include a `Changelog` section for traceability",
                    "add a changelog section with dated version entries",
                )
            else:
                first_entry = find_first_changelog_entry(doc.text, headings)
                if first_entry is None:
                    add_issue(
                        issues,
                        "P1",
                        doc,
                        changelog_heading.line,
                        "frozen_changelog_entry",
                        "Changelog section should start with a dated `- vX.Y (JJ-MM-AAAA)` entry",
                        "add a dated version entry under the changelog section",
                    )
                else:
                    entry_line, latest_version, latest_date = first_entry
                    version = doc.metadata.get("version", "").strip()
                    updated = doc.metadata.get("updated", "").strip()
                    if version and version != latest_version:
                        add_issue(
                            issues,
                            "P1",
                            doc,
                            entry_line,
                            "version_changelog_harmony",
                            f"frontmatter version `{version}` does not match latest changelog entry `{latest_version}`",
                            "align frontmatter version with the latest changelog entry",
                        )
                    if updated and updated != latest_date:
                        add_issue(
                            issues,
                            "P1",
                            doc,
                            entry_line,
                            "updated_changelog_harmony",
                            f"frontmatter updated `{updated}` does not match latest changelog date `{latest_date}`",
                            "align frontmatter updated with the latest changelog date",
                        )

    # Step 3: global ID index and duplicates.
    id_index: dict[str, list[ParsedDoc]] = {}
    for doc in parsed_docs:
        doc_id = doc.metadata.get("id", "").strip()
        if not doc_id:
            continue
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
                "keep one unique id per file across scope",
            )

    # Step 5: depends_on checks.
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

            if not ID_RE.match(dep):
                add_issue(
                    issues,
                    "P1",
                    doc,
                    _line_for(doc.line_map, "depends_on"),
                    "depends_naming",
                    f"depends_on entry is not canonical ID style: {dep}",
                    "normalize dependency ID naming",
                )

            if dep not in id_index and dep not in repo_ids and dep not in allowlist_ids:
                add_issue(
                    issues,
                    "P0",
                    doc,
                    _line_for(doc.line_map, "depends_on"),
                    "depends_ghost",
                    f"depends_on references unknown ID: {dep}",
                    "fix typo, create target file, or add temporary allowlist entry",
                )

    # Sort issues deterministically.
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
        lines.append(f"DocIntegrityChecker {status}")
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
