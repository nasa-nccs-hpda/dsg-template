"""A small CSV inspection example; no client data or external services required."""

import argparse
import csv
import json
from pathlib import Path


def summarize(path: Path) -> dict:
    """Return column names and record count without exposing row contents."""
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.reader(stream)
        columns = next(reader, None)
        if not columns or any(not column.strip() for column in columns):
            raise ValueError("CSV must have a non-empty header for every column")
        if len(set(columns)) != len(columns):
            raise ValueError("CSV column names must be unique")
        rows = 0
        for row in reader:
            if not row:
                continue
            if len(row) != len(columns):
                raise ValueError(f"CSV record ending at line {reader.line_num} has the wrong column count")
            rows += 1
    return {"columns": columns, "rows": rows}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Summarize a CSV file (starter example).")
    parser.add_argument("input", type=Path, help="Path to a UTF-8 CSV file with a header")
    args = parser.parse_args(argv)
    try:
        result = summarize(args.input)
    except (OSError, UnicodeError, ValueError, csv.Error) as error:
        parser.exit(1, f"error: {error}\n")
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
