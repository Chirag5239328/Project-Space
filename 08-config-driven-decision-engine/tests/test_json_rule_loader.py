import tempfile
import os
import json

from core.rules.json_rule_loader import JSONRuleLoader, RuleLoadError


def test_json_rule_loader():

    schema = {
        "age": {"type": "int"},
    }

    rules = {
        "rules": [
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
                "rule_id": "D",
                "priority": 2,
                "decision": "accept",
                "stop_on_match": True,
                "reason": "ok",
                "conditions": [],
            },
        ]
    }

    f = tempfile.NamedTemporaryFile(
    delete=False,
    suffix=".json",
    mode="w",
    encoding="utf-8",
    )


    json.dump(rules, f)
    f.close()

    loader = JSONRuleLoader(schema)

    loaded = loader.load(f.name)

    assert len(loaded) == 2
    assert loaded[0]["rule_id"] == "R1"

    os.remove(f.name)


def test_invalid_rules():

    schema = {
        "age": {"type": "int"},
    }

    bad = {
        "rules": [
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
            }
        ]
    }

    f = tempfile.NamedTemporaryFile(
    delete=False,
    suffix=".json",
    mode="w",
    encoding="utf-8",
    )


    json.dump(bad, f)
    f.close()

    loader = JSONRuleLoader(schema)

    try:
        loader.load(f.name)
        assert False
    except RuleLoadError:
        pass

    os.remove(f.name)
