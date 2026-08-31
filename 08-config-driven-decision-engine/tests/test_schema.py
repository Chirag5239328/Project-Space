import tempfile
import os

from core.schema.schema_inferer import SchemaInferer


def test_schema_inference():

    csv_data = """id,age,salary,active,country
1,25,50000,true,IN
2,30,60000,false,US
"""

    f = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    f.write(csv_data.encode())
    f.close()

    inferer = SchemaInferer()

    schema = inferer.infer(f.name)

    assert schema["id"]["type"] == "int"
    assert schema["age"]["type"] == "int"
    assert schema["salary"]["type"] == "int"
    assert schema["active"]["type"] == "bool"
    assert schema["country"]["type"] == "str"

    os.remove(f.name)
