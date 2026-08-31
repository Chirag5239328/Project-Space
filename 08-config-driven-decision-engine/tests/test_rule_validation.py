import tempfile
import os
import pytest

from core.rules.rules_loader import load_and_validate_rules
from core.rules.rules_loader import RuleConfigError


def _write_yaml(content: str):

    f = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".yaml",
        mode="w",
        encoding="utf-8",
    )

    f.write(content)
    f.close()

    return f.name


def test_valid_rules():

    yaml_data = """
rules:
  - rule_id: R1
    priority: 1
    decision: reject
    stop_on_match: true
    reason: low credit
    conditions:
      all:
        - field: credit_score
          operator: "<"
          value: 600

  - rule_id: DEFAULT
    priority: 999
    decision: accept
    stop_on_match: true
    reason: ok
    conditions:
      all: []
"""

    path = _write_yaml(yaml_data)

    ruleset = load_and_validate_rules(path)

    assert len(ruleset.rules) == 2

    os.remove(path)


def test_duplicate_priority():

    yaml_data = """
rules:
  - rule_id: R1
    priority: 1
    decision: reject
    stop_on_match: true
    reason: bad
    conditions:
      all: []

  - rule_id: R2
    priority: 1
    decision: accept
    stop_on_match: true
    reason: ok
    conditions:
      all: []
"""

    path = _write_yaml(yaml_data)

    with pytest.raises(RuleConfigError):
        load_and_validate_rules(path)

    os.remove(path)
