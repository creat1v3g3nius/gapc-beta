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
    index = 0
    while index < len(body_lines):
        line_no, raw_line = body_lines[index]
        line = raw_line.strip()
        if not line or line.startswith("#"):
            index += 1
            continue
        match = key_value_re.match(raw_line)
        if not match:
            index += 1
            continue

        key = match.group(1).strip()
        value = match.group(2).strip()
        line_map[key] = line_no

        if value:
            metadata[key] = value
            index += 1
            continue

        continuation_items: list[str] = []
        look_ahead = index + 1
        while look_ahead < len(body_lines):
            _, next_raw_line = body_lines[look_ahead]
            next_line = next_raw_line.strip()
            if not next_line or next_line.startswith("#"):
                look_ahead += 1
                continue
            if key_value_re.match(next_raw_line):
                break
            if next_raw_line.startswith((" ", "\t")):
                continuation_items.append(next_line)
            look_ahead += 1

        if continuation_items and all(item.startswith("- ") for item in continuation_items):
            values = [item[2:].strip() for item in continuation_items]
            metadata[key] = "[" + ", ".join(values) + "]"
        elif continuation_items:
            metadata[key] = "\n".join(continuation_items)
        else:
            metadata[key] = value

        index = look_ahead

    return FrontmatterResult(
        metadata=metadata,
        line_map=line_map,
        raw="\n".join(raw for _, raw in body_lines),
        error_code=None,
        error_line=None,
        error_message=None,
    )
