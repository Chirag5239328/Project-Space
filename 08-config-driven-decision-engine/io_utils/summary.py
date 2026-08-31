from collections import Counter
from pathlib import Path
import csv
from typing import List, Union


class SummaryReport:

    def __init__(self, output_path: Union[str, Path]):

        # Normalize to Path
        self.output_path = Path(output_path)

        # Ensure directory exists
        self.output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    def generate(self, decisions: List) -> dict:

        if not decisions:
            raise ValueError("No decisions provided")

        # decisions are Decision objects
        counts = Counter(
            d.decision for d in decisions
        )

        total = len(decisions)

        accept = counts.get("accept", 0)
        reject = counts.get("reject", 0)
        review = counts.get("review", 0)

        report = {
            "total_records": total,
            "accept": accept,
            "reject": reject,
            "review": review,
            "accept_pct": round((accept / total) * 100, 2),
            "reject_pct": round((reject / total) * 100, 2),
            "review_pct": round((review / total) * 100, 2),
        }

        return report

    def write_csv(self, report: dict):

        with self.output_path.open(
            mode="w",
            newline="",
            encoding="utf-8",
        ) as f:

            writer = csv.writer(f)

            writer.writerow(["metric", "value"])

            for k, v in report.items():
                writer.writerow([k, v])
