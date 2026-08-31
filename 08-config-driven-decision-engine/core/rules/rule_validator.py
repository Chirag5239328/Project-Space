from typing import Dict, List, Any

from core.rules.rule_metadata import OPERATOR_REGISTRY


class RuleValidationError(Exception):
    pass


ALLOWED_DECISIONS = {"accept", "reject", "review"}


class RuleValidator:

    def __init__(self, schema: Dict[str, dict]):
        self.schema = schema

    def validate_rules(self, rules: List[Dict]) -> None:

        if not rules:
            raise RuleValidationError("No rules provided")

        self._check_priorities(rules)
        self._check_default_rule(rules)

        for rule in rules:
            self._validate_rule(rule)

    def _check_priorities(self, rules):

        priorities = [r["priority"] for r in rules]

        if len(priorities) != len(set(priorities)):
            raise RuleValidationError("Duplicate priorities found")

    def _check_default_rule(self, rules):

        for r in rules:
            if not r.get("conditions"):
                return

        raise RuleValidationError("No default rule found")

    def _validate_rule(self, rule: Dict):

        required = {
            "rule_id",
            "priority",
            "decision",
            "stop_on_match",
            "conditions",
            "reason",
        }

        missing = required - rule.keys()

        if missing:
            raise RuleValidationError(
                f"Missing fields: {missing}"
            )

        if rule["decision"] not in ALLOWED_DECISIONS:
            raise RuleValidationError(
                f"Invalid decision: {rule['decision']}"
            )

        if not isinstance(rule["priority"], int):
            raise RuleValidationError("Priority must be int")

        if not isinstance(rule["stop_on_match"], bool):
            raise RuleValidationError("stop_on_match must be bool")

        if not isinstance(rule["conditions"], list):
            raise RuleValidationError("conditions must be list")

        for cond in rule["conditions"]:
            self._validate_condition(cond)

    def _validate_condition(self, cond: Dict):

        required = {"field", "operator", "value"}

        missing = required - cond.keys()

        if missing:
            raise RuleValidationError(
                f"Condition missing fields: {missing}"
            )

        field = cond["field"]
        operator = cond["operator"]
        value = cond["value"]

        if field not in self.schema:
            raise RuleValidationError(
                f"Unknown field: {field}"
            )

        field_type = self.schema[field]["type"]

        if field_type not in OPERATOR_REGISTRY:
            raise RuleValidationError(
                f"No operators for {field_type}"
            )

        if operator not in OPERATOR_REGISTRY[field_type]:
            raise RuleValidationError(
                f"Operator {operator} not allowed for {field}"
            )

        self._validate_value(field_type, operator, value)

    def _validate_value(self, field_type, operator, value):

        if operator == "between":

            if (
                not isinstance(value, list)
                or len(value) != 2
            ):
                raise RuleValidationError(
                    "between expects [min, max]"
                )

            for v in value:
                self._check_type(field_type, v)

            return

        if operator in {"in", "not_in"}:

            if not isinstance(value, list):
                raise RuleValidationError(
                    "in expects list"
                )

            for v in value:
                self._check_type(field_type, v)

            return

        self._check_type(field_type, value)

    def _check_type(self, field_type, value):

        if field_type == "int" and not isinstance(value, int):
            raise RuleValidationError(
                f"Expected int, got {type(value)}"
            )

        if field_type == "float" and not isinstance(value, (int, float)):
            raise RuleValidationError(
                f"Expected float, got {type(value)}"
            )

        if field_type == "bool" and not isinstance(value, bool):
            raise RuleValidationError(
                f"Expected bool, got {type(value)}"
            )

        if field_type == "str" and not isinstance(value, str):
            raise RuleValidationError(
                f"Expected str, got {type(value)}"
            )
