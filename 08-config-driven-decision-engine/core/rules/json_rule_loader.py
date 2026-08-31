import json
from typing import List, Dict

from core.rules.rule_validator import RuleValidator, RuleValidationError


class RuleLoadError(Exception):
    pass


class JSONRuleLoader:

    def __init__(self, schema: Dict[str, dict]):
        self.schema = schema
        self.validator = RuleValidator(schema)

    def load(self, path: str) -> List[Dict]:

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

        except Exception as e:
            raise RuleLoadError(f"Cannot read rule file: {e}")

        if "rules" not in data:
            raise RuleLoadError("Missing 'rules' key")

        rules = data["rules"]

        if not isinstance(rules, list):
            raise RuleLoadError("'rules' must be a list")

        try:
            self.validator.validate_rules(rules)

        except RuleValidationError as e:
            raise RuleLoadError(f"Invalid rules: {e}")

        return rules

    def save(self, rules: List[Dict], path: str):

        try:
            self.validator.validate_rules(rules)

            with open(path, "w", encoding="utf-8") as f:
                json.dump(
                    {"rules": rules},
                    f,
                    indent=2,
                )

        except Exception as e:
            raise RuleLoadError(f"Cannot save rules: {e}")
