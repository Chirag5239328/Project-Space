import csv
from typing import Dict, List


class SchemaInferenceError(Exception):
    pass


class SchemaInferer:

    SAMPLE_SIZE = 100  # rows to inspect

    def infer(self, csv_path: str) -> Dict[str, dict]:

        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            if not reader.fieldnames:
                raise SchemaInferenceError("CSV has no headers")

            headers = reader.fieldnames

            samples = []

            for i, row in enumerate(reader):
                samples.append(row)

                if i + 1 >= self.SAMPLE_SIZE:
                    break

            if not samples:
                raise SchemaInferenceError("CSV has no data rows")

        column_values: Dict[str, List[str]] = {
            h: [] for h in headers
        }

        for row in samples:
            for h in headers:
                val = row[h].strip()

                if val != "":
                    column_values[h].append(val)

        schema = {}

        for field, values in column_values.items():

            if not values:
                schema[field] = {"type": "str", "nullable": True}
                continue

            inferred_type = self._infer_type(values)

            schema[field] = {
                "type": inferred_type,
                "nullable": self._has_nulls(samples, field),
            }

        return schema

    def _has_nulls(self, rows, field):

        for r in rows:
            if r[field].strip() == "":
                return True

        return False

    def _infer_type(self, values: List[str]) -> str:

        if self._is_bool(values):
            return "bool"

        if self._is_int(values):
            return "int"

        if self._is_float(values):
            return "float"

        return "str"

    def _is_bool(self, values):

        allowed = {"true", "false", "0", "1"}

        for v in values:
            if v.lower() not in allowed:
                return False

        return True

    def _is_int(self, values):

        for v in values:
            try:
                int(v)
            except ValueError:
                return False

        return True

    def _is_float(self, values):

        for v in values:
            try:
                float(v)
            except ValueError:
                return False

        return True
