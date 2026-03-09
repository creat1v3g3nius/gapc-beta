#!/usr/bin/env python3
"""Validate GAPC vault markdown frontmatter and naming conventions."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from frontmatter_utils import parse_frontmatter_file

REQUIRED_KEYS = (
    "id",
    "type",
    "title",
    "version",
    "status",
    "created",
    "updated",
    "arc",
    "scope",
)

STRICT_REQUIRED_KEYS = ("tags", "depends_on")

ALLOWED_STATUS = {
    "DRAFT",
    "PROPOSED",
    "READY_TO_FREEZE",
    "FROZEN",
    "DEPRECATED",
}

ALLOWED_ARC = {"SYSTEM", "CORE", "PACKAGE", "PRODUCT", "CACHE"}

ARC_BY_PREFIX = {
    "00_SYSTEM": "SYSTEM",
    "01_CORE": "CORE",
    "02_PACKAGE": "PACKAGE",
    "03_PRODUCT": "PRODUCT",
    "99_CACHE": "CACHE",
}

STEM_RE = re.compile(r"^[A-Z0-9_]+$")
TYPE_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
TITLE_RE = re.compile(r"^[A-Z][A-Za-z0-9]*$")
VERSION_RE = re.compile(r"^v\d+\.\d+$")
DATE_RE = re.compile(r"^\d{2}-\d{2}-\d{4}$")
KEY_VALUE_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$")


@dataclass(frozen=True)
class ValidationError:
    path: Path
    line: int
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate vault frontmatter and naming.")
    parser.add_argument(
        "--vault",
        default="vault",
        help="Vault root directory (default: vault)",
    )
    parser.add_argument(
        "--enforce-unique-ids",
        action="store_true",
        help="Fail when the same ID appears in multiple files.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable stricter checks (id==filename, dates, title format, tags/depends_on).",
    )
    return parser.parse_args()


def markdown_files(vault_root: Path) -> list[Path]:
    return sorted(path for path in vault_root.rglob("*.md") if path.is_file())


def read_frontmatter(path: Path) -> tuple[dict[str, str], dict[str, int], list[ValidationError]]:
    result = parse_frontmatter_file(path, KEY_VALUE_RE)
    if result.error_message:
        line = result.error_line if result.error_line is not None else 1
        return {}, {}, [ValidationError(path, line, result.error_message)]
    return result.metadata, result.line_map, []


def parse_date(value: str) -> bool:
    if not DATE_RE.match(value):
        return False
    try:
        dt.datetime.strptime(value, "%d-%m-%Y")
    except ValueError:
        return False
    return True


def expected_arc_for_path(path: Path, vault_root: Path) -> str | None:
    rel_parts = path.relative_to(vault_root).parts
    if not rel_parts:
        return None
    return ARC_BY_PREFIX.get(rel_parts[0])


def validate_file(
    path: Path,
    vault_root: Path,
    strict: bool,
) -> tuple[list[ValidationError], str | None]:
    metadata, key_line, errors = read_frontmatter(path)
    stem = path.stem
    rel_path = path.relative_to(vault_root)

    if not metadata:
        return errors, None

    for key in REQUIRED_KEYS:
        value = metadata.get(key, "").strip()
        if not value:
            errors.append(
                ValidationError(path, key_line.get(key, 1), f"missing required key: {key}")
            )
    if strict:
        for key in STRICT_REQUIRED_KEYS:
            value = metadata.get(key, "").strip()
            if not value:
                errors.append(
                    ValidationError(path, key_line.get(key, 1), f"missing required key: {key}")
                )

    doc_id = metadata.get("id")
    if doc_id:
        if strict and doc_id != stem:
            errors.append(
                ValidationError(
                    path,
                    key_line.get("id", 1),
                    f"id must match filename stem (id={doc_id}, file={stem})",
                )
            )
        if not STEM_RE.match(doc_id):
            errors.append(
                ValidationError(path, key_line.get("id", 1), "id must use [A-Z0-9_]+ pattern")
            )

    if not STEM_RE.match(stem):
        errors.append(
            ValidationError(path, 1, "filename stem must use [A-Z0-9_]+ pattern")
        )

    doc_type = metadata.get("type")
    if doc_type and not TYPE_RE.match(doc_type):
        errors.append(
            ValidationError(path, key_line.get("type", 1), "type must be uppercase token")
        )

    title = metadata.get("title")
    if strict and title and not TITLE_RE.match(title):
        errors.append(
            ValidationError(path, key_line.get("title", 1), "title must be UpperCamelCase")
        )

    version = metadata.get("version")
    if strict and version and not VERSION_RE.match(version):
        errors.append(
            ValidationError(path, key_line.get("version", 1), "version must match vX.Y")
        )

    status = metadata.get("status")
    if status and status not in ALLOWED_STATUS:
        errors.append(
            ValidationError(
                path,
                key_line.get("status", 1),
                f"status must be one of: {', '.join(sorted(ALLOWED_STATUS))}",
            )
        )

    arc = metadata.get("arc")
    if arc and arc not in ALLOWED_ARC:
        errors.append(
            ValidationError(
                path,
                key_line.get("arc", 1),
                f"arc must be one of: {', '.join(sorted(ALLOWED_ARC))}",
            )
        )

    expected_arc = expected_arc_for_path(path, vault_root)
    if strict and arc and expected_arc and arc != expected_arc:
        errors.append(
            ValidationError(
                path,
                key_line.get("arc", 1),
                f"arc/path mismatch: arc={arc}, path={rel_path.parts[0]}",
            )
        )

    for key in ("created", "updated"):
        value = metadata.get(key)
        if strict and value and not parse_date(value):
            errors.append(
                ValidationError(path, key_line.get(key, 1), f"{key} must match JJ-MM-AAAA")
            )

    for key in STRICT_REQUIRED_KEYS:
        value = metadata.get(key)
        if strict and value and not (value.startswith("[") and value.endswith("]")):
            errors.append(
                ValidationError(path, key_line.get(key, 1), f"{key} must be a YAML list")
            )

    scope = metadata.get("scope")
    if strict and scope and not scope.startswith("vault/"):
        errors.append(
            ValidationError(path, key_line.get("scope", 1), "scope must start with vault/")
        )

    return errors, doc_id


def validate(vault_root: Path, enforce_unique_ids: bool, strict: bool) -> int:
    files = markdown_files(vault_root)
    all_errors: list[ValidationError] = []
    id_index: dict[str, list[Path]] = defaultdict(list)

    for path in files:
        errors, doc_id = validate_file(path, vault_root, strict)
        all_errors.extend(errors)
        if doc_id:
            id_index[doc_id].append(path)

    if enforce_unique_ids:
        for doc_id, paths in sorted(id_index.items()):
            if len(paths) <= 1:
                continue
            first = paths[0]
            for duplicate in paths[1:]:
                all_errors.append(
                    ValidationError(
                        duplicate,
                        1,
                        f"duplicate id '{doc_id}' (already used by {first.relative_to(vault_root)})",
                    )
                )

    if all_errors:
        for error in sorted(all_errors, key=lambda item: (str(item.path), item.line, item.message)):
            print(f"ERROR {error.path}:{error.line} {error.message}")
        print(f"FAIL {len(all_errors)} error(s) across {len(files)} file(s)")
        return 1

    print(f"PASS validated {len(files)} markdown file(s) in {vault_root}")
    return 0


def main() -> int:
    args = parse_args()
    vault_root = Path(args.vault).resolve()
    if not vault_root.exists() or not vault_root.is_dir():
        print(f"FAIL vault path does not exist: {vault_root}")
        return 2
    return validate(vault_root, args.enforce_unique_ids, args.strict)


if __name__ == "__main__":
    sys.exit(main())
