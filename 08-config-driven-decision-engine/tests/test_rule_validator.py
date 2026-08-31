import pytest

from core.rules.rule_validator import RuleValidator, RuleValidationError


def test_valid_rules():

    schema = {
        "age": {"type": "int"},
        "active": {"type": "bool"},
    }

    rules = [
        {
            "rule_id": "R1",
            "priority": 1,
            "decision": "reject",
            "stop_on_match": True,
            "reason": "young",
            "conditions": [
                {
                    "field": "age",
                    "operator": "<",
                    "value": 18,
                }
            ],
        },
        {
            "rule_id": "DEFAULT",
            "priority": 2,
            "decision": "accept",
            "stop_on_match": True,
            "reason": "ok",
            "conditions": [],
        },
    ]

    v = RuleValidator(schema)

    v.validate_rules(rules)


def test_invalid_field():

    schema = {"age": {"type": "int"}}

    rules = [
        {
            "rule_id": "R1",
            "priority": 1,
            "decision": "reject",
            "stop_on_match": True,
            "reason": "bad",
            "conditions": [
                {
                    "field": "salary",
                    "operator": "<",
                    "value": 10,
                }
            ],
        },
        {
            "rule_id": "D",
            "priority": 2,
            "decision": "accept",
            "stop_on_match": True,
            "reason": "ok",
            "conditions": [],
        },
    ]

    v = RuleValidator(schema)

    with pytest.raises(RuleValidationError):
        v.validate_rules(rules)
