from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

REQUIRED_FIELDS = {"timestamp", "device", "sensor", "value", "unit"}


def load_jsonl(path: Path) -> pd.DataFrame:
    records = []
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                print(f"Line {line_number}: invalid JSON: {error}", file=sys.stderr)
                continue

            if not REQUIRED_FIELDS.issubset(record):
                print(f"Line {line_number}: missing required fields", file=sys.stderr)
                continue

            try:
                value = float(record["value"])
            except (TypeError, ValueError):
                print(f"Line {line_number}: value is not numeric", file=sys.stderr)
                continue

            if not pd.notna(value) or not 0 <= value <= 100:
                print(f"Line {line_number}: value outside accepted range", file=sys.stderr)
                continue

            record["value"] = value
            records.append(record)

    return pd.DataFrame(records)


def main() -> None:
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("capstone/data/readings.jsonl")
    output_dir = Path("capstone/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    frame = load_jsonl(source)
    if frame.empty:
        raise SystemExit("No valid records found")

    frame["timestamp"] = pd.to_datetime(frame["timestamp"], errors="coerce", utc=True)
    frame = frame.dropna(subset=["timestamp"]).sort_values("timestamp")

    summary = (
        frame.groupby(["device", "sensor", "unit"])["value"]
        .agg(["count", "mean", "median", "min", "max", "std"])
        .reset_index()
    )
    summary.to_csv(output_dir / "summary.csv", index=False)

    plt.figure(figsize=(10, 5))
    plt.plot(frame["timestamp"], frame["value"], marker=".", linewidth=1)
    plt.title("Simulated Flow Sensor Readings")
    plt.xlabel("Time (UTC)")
    plt.ylabel("Flow rate (L/min)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_dir / "timeseries.png", dpi=160)

    print(f"Valid records: {len(frame)}")
    print(summary.to_string(index=False))
    print(f"Output directory: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
