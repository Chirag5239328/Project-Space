from core.rules.rule_adapter import RuleAdapter


def test_rule_adapter():

    json_rules = [
        {
            "rule_id": "R1",
            "priority": 1,
            "decision": "reject",
            "stop_on_match": True,
            "reason": "bad",
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

    adapter = RuleAdapter()

    ruleset = adapter.adapt(json_rules)

    assert len(ruleset.rules) == 2

    assert ruleset.rules[0].rule_id == "R1"
    assert ruleset.rules[1].decision == "accept"
