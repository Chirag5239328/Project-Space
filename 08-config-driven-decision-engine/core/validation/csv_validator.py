import csv
from typing import List
from pydantic import ValidationError

from core.schema.record_schema import Record

REQUIRED_HEADERS = [
    "record_id",
    "age",
    "annual_income",
    "credit_score",
    "country",
    "kyc_verified",
    "requested_amount",
    "employment_type",
]


class CSVValidationError(Exception):
    pass


def validate_headers(headers: List[str]):
    if headers != REQUIRED_HEADERS:
        raise CSVValidationError(
            f"Invalid CSV headers.\nExpected: {REQUIRED_HEADERS}\nFound: {headers}"
        )


def validate_csv(path: str) -> List[Record]:
    records: List[Record] = []
    seen_ids = set()

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None:
            raise CSVValidationError("CSV file has no headers")

        validate_headers(reader.fieldnames)

        for line_number, row in enumerate(reader, start=2):
            try:
                if row["record_id"] in seen_ids:
                    raise CSVValidationError(
                        f"Duplicate record_id '{row['record_id']}' at line {line_number}"
                    )

                record = Record(
                    record_id=row["record_id"],
                    age=int(row["age"]),
                    annual_income=int(row["annual_income"]),
                    credit_score=int(row["credit_score"]),
                    country=row["country"],
                    kyc_verified=row["kyc_verified"].lower() == "true",
                    requested_amount=int(row["requested_amount"]),
                    employment_type=row["employment_type"],
                )

                seen_ids.add(record.record_id)
                records.append(record)

            except ValidationError as e:
                raise CSVValidationError(
                    f"Validation error at line {line_number}: {e}"
                ) from e
            except ValueError as e:
                raise CSVValidationError(
                    f"Type conversion error at line {line_number}: {e}"
                ) from e

    if not records:
        raise CSVValidationError("CSV contains no data rows")

    return records
