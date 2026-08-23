#!/usr/bin/env python3
"""Validate keymap binding counts and documented physical coordinates."""

import re
import sys
from pathlib import Path


KEYMAP_PATH = Path(__file__).resolve().parents[1] / "config" / "keymap.keymap"
ROW_COORDINATES = (
    (0, (0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13)),
    (1, (0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13)),
    (2, tuple(range(14))),
    (3, (0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13)),
)
LAYER_PATTERN = re.compile(
    r"\b(layer_[A-Za-z0-9_]+)\s*\{.*?bindings\s*=\s*<(.*?)>;.*?\};",
    re.DOTALL,
)
BINDING_PATTERN = re.compile(r"&[A-Za-z0-9_]+")


def parse_bindings(body: str) -> list[str]:
    body = re.sub(r"/\*.*?\*/|//.*?$", "", body, flags=re.DOTALL | re.MULTILINE)
    starts = [match.start() for match in BINDING_PATTERN.finditer(body)]
    return [
        re.sub(r"\s+", " ", body[start : starts[index + 1] if index + 1 < len(starts) else None]).strip()
        for index, start in enumerate(starts)
    ]


def main() -> int:
    source = KEYMAP_PATH.read_text(encoding="utf-8")
    layers = list(LAYER_PATTERN.finditer(source))
    expected_count = sum(len(columns) for _, columns in ROW_COORDINATES)
    errors = []
    parsed_layers: dict[str, list[str]] = {}

    if not layers:
        errors.append("no keymap layers found")

    for layer in layers:
        layer_name = layer.group(1)
        bindings = parse_bindings(layer.group(2))
        parsed_layers[layer_name] = bindings
        count = len(bindings)
        if count != expected_count:
            errors.append(f"{layer_name}: expected {expected_count} bindings, found {count}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(layers)} layers ({expected_count} bindings each)")

    if len(sys.argv) == 4:
        layer_name, row_arg, column_arg = sys.argv[1:]
        try:
            row = int(row_arg.removeprefix("r"))
            column = int(column_arg.removeprefix("c"))
            offset = 0
            position = None
            for physical_row, columns in ROW_COORDINATES:
                if physical_row == row and column in columns:
                    position = offset + columns.index(column)
                    break
                offset += len(columns)
            if position is None:
                raise ValueError("coordinate has no physical key")
            print(f"{layer_name} r{row} c{column}: {parsed_layers[layer_name][position]}")
        except (KeyError, ValueError) as error:
            print(f"error: invalid coordinate: {error}", file=sys.stderr)
            return 2
    elif len(sys.argv) != 1:
        print(f"usage: {Path(sys.argv[0]).name} [LAYER ROW COLUMN]", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
