#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate scenario.json against schemas/scenario.schema.json.")
    parser.add_argument("scenario_json", type=Path, help="Path to scenario.json")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("schemas/scenario.schema.json"),
        help="Path to scenario schema JSON",
    )
    args = parser.parse_args()

    try:
        import jsonschema
    except ModuleNotFoundError:
        print(
            "Missing dependency: jsonschema. Install it with `python3 -m pip install jsonschema`.",
            file=sys.stderr,
        )
        return 2

    try:
        schema = json.loads(args.schema.read_text(encoding="utf-8"))
        payload = json.loads(args.scenario_json.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        print(f"File not found: {exc.filename}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON: {exc}", file=sys.stderr)
        return 1

    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(payload), key=lambda item: list(item.path))
    if errors:
        print(f"{args.scenario_json} failed schema validation:", file=sys.stderr)
        for error in errors:
            location = "/".join(str(part) for part in error.absolute_path) or "<root>"
            print(f"- {location}: {error.message}", file=sys.stderr)
        return 1

    print(f"{args.scenario_json} is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
