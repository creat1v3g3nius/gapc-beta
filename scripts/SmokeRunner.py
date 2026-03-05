#!/usr/bin/env python3
"""Run a fast GAPC smoke test for repo/vault/tooling health."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


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
    return parser.parse_args()


def _ok(message: str) -> None:
    print(f"OK   {message}")


def _ko(message: str) -> None:
    print(f"KO   {message}")


def ensure_exists(path: Path, kind: str = "path") -> None:
    if not path.exists():
        raise SmokeFailure(f"missing {kind}: {path}")


def run_validator(repo_root: Path, validator_rel: str) -> None:
    validator = (repo_root / validator_rel).resolve()
    ensure_exists(validator, "validator")

    cmd = [str(validator)]
    try:
        result = subprocess.run(cmd, cwd=repo_root, check=False)
    except PermissionError:
        # Fallback if executable bit is missing on another machine.
        result = subprocess.run(["python3", str(validator)], cwd=repo_root, check=False)

    if result.returncode != 0:
        raise SmokeFailure(f"validator failed with exit code {result.returncode}")


def check_arcs(vault_root: Path) -> None:
    required = ["00_SYSTEM", "01_CORE", "02_PACKAGE", "03_PRODUCT"]
    for arc in required:
        ensure_exists(vault_root / arc, "arc")
    # Support both conventions; current repo uses 99_CACHE.
    if not (vault_root / "99_CACHE").exists() and not (vault_root / "04_CACHE").exists():
        raise SmokeFailure("missing cache arc: expected vault/99_CACHE or vault/04_CACHE")


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

        run_validator(repo_root, args.validator)
        _ok("validator execution")

    except SmokeFailure as err:
        _ko(str(err))
        print("FAIL smoke runner")
        return 1

    print("PASS smoke runner")
    return 0


if __name__ == "__main__":
    sys.exit(run())
