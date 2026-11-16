"""Evidence ledger for documenting observed AI and robotics impacts.

The tool stores sourced observations; it does not estimate a universal
"AI impact score" or infer causal effects from unrelated measurements.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
import tempfile
import uuid
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

DIRECTIONS = {"benefit", "harm", "mixed", "unknown"}
VERIFICATION = {"reported", "independently_verified"}


@dataclass(frozen=True)
class Observation:
    id: str
    system: str
    sector: str
    indicator: str
    direction: str
    value: float
    unit: str
    period_start: str
    period_end: str
    population: str
    method: str
    source_url: str
    verification: str
    notes: str = ""
    recorded_at: str = ""

    @classmethod
    def create(cls, **values: Any) -> "Observation":
        values.setdefault("id", str(uuid.uuid4()))
        values.setdefault("recorded_at", datetime.now(timezone.utc).isoformat())
        item = cls(**values)
        item.validate()
        return item

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Observation":
        if not isinstance(raw, dict):
            raise ValueError("each observation must be a JSON object")
        allowed = set(cls.__dataclass_fields__)
        unknown = set(raw) - allowed
        if unknown:
            raise ValueError(f"unknown observation fields: {', '.join(sorted(unknown))}")
        item = cls(**raw)
        item.validate()
        return item

    def validate(self) -> None:
        for key in ("id", "system", "sector", "indicator", "unit", "population", "method", "source_url"):
            value = getattr(self, key)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{key} must be a non-empty string")
        if self.direction not in DIRECTIONS:
            raise ValueError(f"direction must be one of: {', '.join(sorted(DIRECTIONS))}")
        if self.verification not in VERIFICATION:
            raise ValueError(f"verification must be one of: {', '.join(sorted(VERIFICATION))}")
        if isinstance(self.value, bool) or not isinstance(self.value, (int, float)) or not math.isfinite(self.value):
            raise ValueError("value must be a finite number")
        try:
            start = date.fromisoformat(self.period_start)
            end = date.fromisoformat(self.period_end)
        except (TypeError, ValueError) as exc:
            raise ValueError("period_start and period_end must be ISO dates (YYYY-MM-DD)") from exc
        if end < start:
            raise ValueError("period_end cannot be earlier than period_start")
        parsed = urlparse(self.source_url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("source_url must be an absolute HTTP(S) URL")
        if self.recorded_at:
            try:
                datetime.fromisoformat(self.recorded_at.replace("Z", "+00:00"))
            except ValueError as exc:
                raise ValueError("recorded_at must be an ISO-8601 timestamp") from exc


def load_ledger(path: Path) -> list[Observation]:
    if not path.exists():
        return []
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError("ledger root must be a JSON array")
    items = [Observation.from_dict(item) for item in raw]
    ids = [item.id for item in items]
    if len(ids) != len(set(ids)):
        raise ValueError("ledger contains duplicate observation IDs")
    return items


def save_ledger(path: Path, items: list[Observation]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps([asdict(item) for item in items], indent=2, ensure_ascii=False) + "\n"
    temp_name = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as stream:
            temp_name = stream.name
            stream.write(payload)
            stream.flush()
        Path(temp_name).replace(path)
    finally:
        if temp_name and Path(temp_name).exists():
            Path(temp_name).unlink()


def build_report(items: list[Observation]) -> dict[str, Any]:
    grouped: dict[tuple[str, str, str, str, str, str], list[Observation]] = defaultdict(list)
    for item in items:
        # Do not pool observations from different populations or study methods.
        grouped[(item.system, item.sector, item.indicator, item.unit, item.population, item.method)].append(item)
    groups = []
    for (system, sector, indicator, unit, population, method), records in sorted(grouped.items()):
        values = [float(record.value) for record in records]
        groups.append({
            "system": system,
            "sector": sector,
            "indicator": indicator,
            "unit": unit,
            "population": population,
            "method": method,
            "period_start": min(record.period_start for record in records),
            "period_end": max(record.period_end for record in records),
            "observation_count": len(records),
            "min": min(values),
            "max": max(values),
            "mean": round(sum(values) / len(values), 6),
            "directions": {direction: sum(record.direction == direction for record in records) for direction in sorted(DIRECTIONS)},
            "independently_verified_count": sum(record.verification == "independently_verified" for record in records),
            "source_urls": sorted({record.source_url for record in records}),
        })
    return {
        "observation_count": len(items),
        "group_count": len(groups),
        "groups": groups,
        "interpretation": "Descriptive summaries only. Groups are separated by system, sector, indicator, unit, population and method; values are not combined across unlike measurements or into a universal AI-impact score and do not establish causality.",
    }


def _add(args: argparse.Namespace) -> int:
    item = Observation.create(
        system=args.system, sector=args.sector, indicator=args.indicator,
        direction=args.direction, value=args.value, unit=args.unit,
        period_start=args.period_start, period_end=args.period_end,
        population=args.population, method=args.method, source_url=args.source_url,
        verification=args.verification, notes=args.notes,
    )
    items = load_ledger(args.ledger)
    items.append(item)
    save_ledger(args.ledger, items)
    print(json.dumps(asdict(item), indent=2, ensure_ascii=False))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Record sourced observations about AI and robotics impacts.")
    parser.add_argument("--ledger", type=Path, default=Path("data/observations.json"))
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add", help="append one sourced observation")
    for flag, help_text in [
        ("system", "AI/robotics system or intervention name"),
        ("sector", "sector or domain"),
        ("indicator", "measured indicator name"),
        ("unit", "unit for the value"),
        ("period-start", "measurement period start (YYYY-MM-DD)"),
        ("period-end", "measurement period end (YYYY-MM-DD)"),
        ("population", "population or scope measured"),
        ("method", "measurement method or study design"),
        ("source-url", "source URL supporting this observation"),
    ]:
        add.add_argument("--" + flag, required=True, help=help_text)
    add.add_argument("--direction", required=True, choices=sorted(DIRECTIONS))
    add.add_argument("--verification", default="reported", choices=sorted(VERIFICATION))
    add.add_argument("--value", required=True, type=float)
    add.add_argument("--notes", default="")
    sub.add_parser("list", help="list stored observations")
    sub.add_parser("report", help="summarize compatible indicator groups")
    export = sub.add_parser("export-csv", help="export observations to CSV")
    export.add_argument("output", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "add":
            return _add(args)
        items = load_ledger(args.ledger)
        if args.command == "list":
            print(json.dumps([asdict(item) for item in items], indent=2, ensure_ascii=False))
        elif args.command == "report":
            print(json.dumps(build_report(items), indent=2, ensure_ascii=False))
        elif args.command == "export-csv":
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with args.output.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=list(Observation.__dataclass_fields__))
                writer.writeheader()
                writer.writerows(asdict(item) for item in items)
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"asimov-meter: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
