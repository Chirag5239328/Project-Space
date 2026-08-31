import csv
from pathlib import Path
from typing import List, Dict, Union


class OutputWriter:

    def __init__(self, output_path: Union[str, Path]):

        # Always normalize to Path
        self.output_path = Path(output_path)

        # Ensure directory exists
        self.output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    def write(
        self,
        records: List[Dict],
        decisions: List,
    ):

        if len(records) != len(decisions):
            raise ValueError(
                "Records and decisions count do not match"
            )

        if not records:
            raise ValueError("No records to write")

        fieldnames = list(records[0].keys()) + [
            "decision",
            "rule_id",
            "reason",
        ]

        with self.output_path.open(
            mode="w",
            newline="",
            encoding="utf-8",
        ) as f:

            writer = csv.DictWriter(
                f,
                fieldnames=fieldnames,
            )

            writer.writeheader()

            for record, decision in zip(records, decisions):

                row = record.copy()

                # decision is Decision object
                row["decision"] = decision.decision
                row["rule_id"] = decision.rule_id
                row["reason"] = decision.reason

                writer.writerow(row)
