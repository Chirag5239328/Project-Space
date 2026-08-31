import yaml
from pydantic import ValidationError

from core.rules.rule_schema import RuleSet


class RuleConfigError(Exception):
    pass


def load_and_validate_rules(path: str) -> RuleSet:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        raise RuleConfigError(f"Failed to load rules file: {e}")

    if not isinstance(data, dict) or "rules" not in data:
        raise RuleConfigError("rules.yaml must contain a top-level 'rules' key")

    try:
        ruleset = RuleSet(**data)
    except ValidationError as e:
        raise RuleConfigError(f"Rule validation error: {e}") from e

    return ruleset
