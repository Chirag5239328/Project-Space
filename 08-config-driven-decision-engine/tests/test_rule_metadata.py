from core.rules.rule_metadata import RuleMetadataService


def test_metadata():

    schema = {
        "age": {"type": "int"},
        "active": {"type": "bool"},
        "country": {"type": "str"},
    }

    service = RuleMetadataService(schema)

    fields = service.get_fields()
    ops = service.get_allowed_operators()

    assert "age" in fields
    assert "<" in ops["age"]

    assert "==" in ops["active"]

    assert "in" in ops["country"]
