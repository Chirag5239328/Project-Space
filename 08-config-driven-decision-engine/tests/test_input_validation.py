import tempfile
import os
import pytest

from core.validation.csv_validator import validate_csv
from core.validation.csv_validator import CSVValidationError


def _write_csv(content: str):

    f = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".csv",
        mode="w",
        encoding="utf-8",
    )

    f.write(content)
    f.close()

    return f.name


def test_valid_input():

    csv_data = """record_id,age,annual_income,credit_score,country,kyc_verified,requested_amount,employment_type
R1,25,300000,700,IN,true,200000,salaried
"""

    path = _write_csv(csv_data)

    records = validate_csv(path)

    assert len(records) == 1

    os.remove(path)


def test_invalid_credit_score():

    csv_data = """record_id,age,annual_income,credit_score,country,kyc_verified,requested_amount,employment_type
R1,25,300000,100,IN,true,200000,salaried
"""

    path = _write_csv(csv_data)

    with pytest.raises(CSVValidationError):
        validate_csv(path)

    os.remove(path)
