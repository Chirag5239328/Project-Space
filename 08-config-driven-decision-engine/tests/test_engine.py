from engine.evaluator import RuleEvaluator
from core.rules.rule_schema import RuleSet
from core.schema.record_schema import Record
from audit.db import init_db
from audit.logger import AuditLogger


def test_priority_resolution():

    rules_data = {
        "rules": [
            {
                "rule_id": "REJECT",
                "priority": 1,
                "decision": "reject",
                "stop_on_match": True,
                "reason": "bad",
                "conditions": {
                    "all": [
                        {
                            "field": "credit_score",
                            "operator": "<",
                            "value": 700,
                        }
                    ]
                },
            },
            {
                "rule_id": "REVIEW",
                "priority": 2,
                "decision": "review",
                "stop_on_match": True,
                "reason": "maybe",
                "conditions": {"all": []},
            },
        ]
    }

    ruleset = RuleSet(**rules_data)

    init_db()
    logger = AuditLogger()

    engine = RuleEvaluator(ruleset, logger)

    record = Record(
        record_id="R1",
        age=30,
        annual_income=300000,
        credit_score=650,
        country="IN",
        kyc_verified=True,
        requested_amount=200000,
        employment_type="salaried",
    )

    result = engine.evaluate(record)

    logger.close()

    assert result.decision == "reject"
