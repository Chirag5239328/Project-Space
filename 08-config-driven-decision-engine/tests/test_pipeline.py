import tempfile
import os

from core.validation.csv_validator import validate_csv
from core.rules.rules_loader import load_and_validate_rules
from engine.evaluator import RuleEvaluator
from audit.db import init_db
from audit.logger import AuditLogger


def test_full_pipeline():

    csv_data = """record_id,age,annual_income,credit_score,country,kyc_verified,requested_amount,employment_type
R1,35,400000,720,IN,true,200000,salaried
"""

    rules_data = """
rules:
  - rule_id: LOW
    priority: 1
    decision: reject
    stop_on_match: true
    reason: bad
    conditions:
      all:
        - field: credit_score
          operator: "<"
          value: 600

  - rule_id: DEFAULT
    priority: 2
    decision: accept
    stop_on_match: true
    reason: ok
    conditions:
      all: []
"""

    csv_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    csv_file.write(csv_data.encode())
    csv_file.close()

    yaml_file = tempfile.NamedTemporaryFile(delete=False, suffix=".yaml")
    yaml_file.write(rules_data.encode())
    yaml_file.close()

    records = validate_csv(csv_file.name)
    rules = load_and_validate_rules(yaml_file.name)

    init_db()
    logger = AuditLogger()

    engine = RuleEvaluator(rules, logger)

    result = engine.evaluate(records[0])

    logger.close()

    assert result.decision == "accept"

    os.remove(csv_file.name)
    os.remove(yaml_file.name)
