import tempfile
import os
import csv

from core.schema.schema_inferer import SchemaInferer
from core.validation.dynamic_validator import DynamicValidator


def test_dynamic_validation():

    csv_data = """id,age,active
1,25,true
2,30,false
"""

    f = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    f.write(csv_data.encode())
    f.close()

    inferer = SchemaInferer()
    schema = inferer.infer(f.name)

    validator = DynamicValidator(schema)

    with open(f.name, newline="") as file:
        reader = csv.DictReader(file)

        rows = list(reader)

    rec1 = validator.validate(rows[0])
    rec2 = validator.validate(rows[1])

    assert rec1.age == 25
    assert rec1.active is True

    assert rec2.age == 30
    assert rec2.active is False

    os.remove(f.name)
