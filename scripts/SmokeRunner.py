#!/usr/bin/env python3
"""Run a fast GAPC smoke test for repo/vault/tooling health."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from frontmatter_utils import parse_frontmatter_file


class SmokeFailure(Exception):
    """Raised when a smoke check fails."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GAPC smoke runner")
    parser.add_argument("--repo-root", default=".", help="Repo root path (default: current directory)")
    parser.add_argument("--vault", default="vault", help="Vault directory relative to repo root")
    parser.add_argument(
        "--validator",
        default="scripts/ValidateFrontmatter.py",
        help="Validator command path relative to repo root",
    )
    parser.add_argument(
        "--require-path",
        action="append",
        default=[],
        help="Extra required path (relative to repo root). Can be repeated.",
    )
    parser.add_argument(
        "--run-doc-integrity",
        action="store_true",
        help="Run DocIntegrityChecker as part of smoke checks.",
    )
    parser.add_argument(
        "--doc-integrity-script",
        default="scripts/DocIntegrityChecker.py",
        help="DocIntegrityChecker command path relative to repo root.",
    )
    parser.add_argument(
        "--doc-integrity-scope",
        default="vault",
        help="Scope passed to DocIntegrityChecker (default: vault).",
    )
    parser.add_argument(
        "--doc-integrity-max-exit",
        type=int,
        default=2,
        choices=(0, 1, 2),
        help=(
            "Highest acceptable DocIntegrityChecker exit code. "
            "0=PASS only, 1=PASS+FAIL threshold, 2=PASS/WARN accepted (default)."
        ),
    )
    parser.add_argument(
        "--check-pre-freeze",
        action="store_true",
        help=(
            "Enable strict pre-freeze status gate: outside CACHE, "
            "status must be FROZEN and DEPRECATED is forbidden."
        ),
    )
    return parser.parse_args()


def _ok(message: str) -> None:
    print(f"OK   {message}")


def _ko(message: str) -> None:
    print(f"KO   {message}")


def ensure_exists(path: Path, kind: str = "path") -> None:
    if not path.exists():
        raise SmokeFailure(f"missing {kind}: {path}")


def run_validator(repo_root: Path, validator_rel: str, vault_rel: str) -> None:
    validator = (repo_root / validator_rel).resolve()
    ensure_exists(validator, "validator")

    cmd = [str(validator), "--vault", vault_rel, "--strict"]
    try:
        result = subprocess.run(cmd, cwd=repo_root, check=False)
    except PermissionError:
        # Fallback if executable bit is missing on another machine.
        result = subprocess.run(["python3", str(validator), *cmd[1:]], cwd=repo_root, check=False)

    if result.returncode != 0:
        raise SmokeFailure(f"validator failed with exit code {result.returncode}")


def run_doc_integrity(
    repo_root: Path,
    checker_rel: str,
    checker_scope: str,
    max_exit: int,
) -> int:
    checker = (repo_root / checker_rel).resolve()
    ensure_exists(checker, "doc integrity checker")

    cmd = [str(checker), "--scope", checker_scope, "--output", "text", "--min-severity", "P1"]
    try:
        result = subprocess.run(cmd, cwd=repo_root, check=False)
    except PermissionError:
        # Fallback if executable bit is missing on another machine.
        result = subprocess.run(["python3", str(checker), *cmd[1:]], cwd=repo_root, check=False)

    if result.returncode > max_exit:
        raise SmokeFailure(
            "doc integrity checker failed with exit code "
            f"{result.returncode} (max allowed: {max_exit})"
        )

    return result.returncode


def check_arcs(vault_root: Path) -> None:
    required = ["00_SYSTEM", "01_CORE", "02_PACKAGE", "03_PRODUCT"]
    for arc in required:
        ensure_exists(vault_root / arc, "arc")
    # Support both conventions; current repo uses 99_CACHE.
    if not (vault_root / "99_CACHE").exists() and not (vault_root / "04_CACHE").exists():
        raise SmokeFailure("missing cache arc: expected vault/99_CACHE or vault/04_CACHE")


def _is_cache_file(path: Path, vault_root: Path) -> bool:
    rel = path.relative_to(vault_root)
    if not rel.parts:
        return False
    return rel.parts[0] in {"99_CACHE", "04_CACHE"}


def _read_status(path: Path) -> str | None:
    result = parse_frontmatter_file(path)
    if result.error_message:
        return None
    raw = result.metadata.get("status", "").strip()
    if not raw:
        return None
    if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
        raw = raw[1:-1].strip()
    return raw or None


def check_pre_freeze_status(vault_root: Path) -> None:
    not_frozen: list[Path] = []
    deprecated_outside_cache: list[Path] = []
    missing_status: list[Path] = []

    for path in sorted(vault_root.rglob("*.md")):
        if _is_cache_file(path, vault_root):
            continue

        status = _read_status(path)
        if status is None:
            missing_status.append(path)
            continue

        if status == "DEPRECATED":
            deprecated_outside_cache.append(path)
        if status != "FROZEN":
            not_frozen.append(path)

    if not_frozen or deprecated_outside_cache or missing_status:
        samples: list[str] = []
        for group in (not_frozen, deprecated_outside_cache, missing_status):
            for sample in group[:2]:
                samples.append(str(sample.relative_to(vault_root)))

        raise SmokeFailure(
            "pre-freeze status gate failed: "
            f"outside-cache status!=FROZEN: {len(not_frozen)}, "
            f"outside-cache DEPRECATED: {len(deprecated_outside_cache)}, "
            f"outside-cache missing status/frontmatter: {len(missing_status)}; "
            f"examples: {', '.join(samples) if samples else 'n/a'}"
        )


def run() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()

    try:
        ensure_exists(repo_root, "repo root")
        ensure_exists(repo_root / ".git", ".git")
        _ok("git root detected")

        vault_root = repo_root / args.vault
        ensure_exists(vault_root, "vault")
        _ok("vault present")

        check_arcs(vault_root)
        _ok("required vault arcs present")

        ensure_exists(repo_root / ".vscode" / "settings.json", "VS Code settings")
        ensure_exists(repo_root / ".vscode" / "tasks.json", "VS Code tasks")
        _ok("VS Code bootstrap files present")

        ensure_exists(repo_root / "scripts" / "ValidateFrontmatter.py", "validator script")
        _ok("validator script present")

        for rel_path in args.require_path:
            ensure_exists(repo_root / rel_path, "required path")
        if args.require_path:
            _ok("extra required paths present")

        run_validator(repo_root, args.validator, args.vault)
        _ok("validator execution")

        if args.check_pre_freeze:
            check_pre_freeze_status(vault_root)
            _ok("pre-freeze status gate")

        should_run_doc_integrity = args.run_doc_integrity or args.check_pre_freeze
        if should_run_doc_integrity:
            doc_exit = run_doc_integrity(
                repo_root=repo_root,
                checker_rel=args.doc_integrity_script,
                checker_scope=args.doc_integrity_scope,
                max_exit=args.doc_integrity_max_exit,
            )
            if doc_exit == 0:
                _ok("doc integrity execution")
            elif doc_exit == 2:
                _ok("doc integrity execution (WARN accepted)")
            else:
                _ok("doc integrity execution (non-blocking threshold applied)")

    except SmokeFailure as err:
        _ko(str(err))
        print("FAIL smoke runner")
        return 1

    print("PASS smoke runner")
    return 0


if __name__ == "__main__":
    sys.exit(run())
