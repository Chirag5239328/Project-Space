import sys
from core.schema.schema_inferer import SchemaInferer


if len(sys.argv) != 2:
    print("Usage: python inspect_schema.py <csv_file>")
    sys.exit(1)


path = sys.argv[1]

inferer = SchemaInferer()

schema = inferer.infer(path)

print("Inferred Schema:\n")

for field, meta in schema.items():
    print(f"{field}: {meta}")
