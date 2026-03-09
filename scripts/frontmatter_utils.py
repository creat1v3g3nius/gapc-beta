#!/usr/bin/env python3
"""Shared frontmatter parsing helpers for GAPC scripts."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Pattern

DEFAULT_KEY_VALUE_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$")


@dataclass(frozen=True)
class FrontmatterResult:
    metadata: dict[str, str]
    line_map: dict[str, int]
    raw: str
    error_code: str | None
    error_line: int | None
    error_message: str | None


def parse_frontmatter_file(
    path: Path,
    key_value_re: Pattern[str] = DEFAULT_KEY_VALUE_RE,
) -> FrontmatterResult:
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        first = handle.readline()
        if not first or first.strip() != "---":
            return FrontmatterResult(
                metadata={},
                line_map={},
                raw="",
                error_code="missing_opening",
                error_line=1,
                error_message="frontmatter missing (expected opening ---)",
            )

        body_lines: list[tuple[int, str]] = []
        closing_line: int | None = None
        for line_no, raw_line in enumerate(handle, start=2):
            if raw_line.strip() == "---":
                closing_line = line_no
                break
            body_lines.append((line_no, raw_line.rstrip("\n")))

    if closing_line is None:
        return FrontmatterResult(
            metadata={},
            line_map={},
            raw="",
            error_code="missing_closing",
            error_line=1,
            error_message="frontmatter missing closing ---",
        )

    metadata: dict[str, str] = {}
    line_map: dict[str, int] = {}
    for line_no, raw_line in body_lines:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        match = key_value_re.match(raw_line)
        if not match:
            continue
        key = match.group(1).strip()
        value = match.group(2).strip()
        metadata[key] = value
        line_map[key] = line_no

    return FrontmatterResult(
        metadata=metadata,
        line_map=line_map,
        raw="\n".join(raw for _, raw in body_lines),
        error_code=None,
        error_line=None,
        error_message=None,
    )
