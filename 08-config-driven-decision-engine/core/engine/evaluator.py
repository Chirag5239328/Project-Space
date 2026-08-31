from typing import Dict, Any, List, Optional, Union

from core.engine.operators import OPERATOR_MAP
from core.rules.rule_schema import RuleSet, Rule, Condition
from audit.logger import AuditLogger


class RuleEvaluationError(Exception):
    pass


class DecisionResult:

    def __init__(self, decision: str, rule_id: str, reason: str):
        self.decision = decision
        self.rule_id = rule_id
        self.reason = reason

    def to_dict(self) -> Dict[str, str]:

        return {
            "decision": self.decision,
            "rule_id": self.rule_id,
            "reason": self.reason,
        }


class RuleEvaluator:

    def __init__(self, ruleset: RuleSet, audit_logger: AuditLogger):

        self.rules: List[Rule] = sorted(
            ruleset.rules, key=lambda r: r.priority
        )

        self.audit_logger = audit_logger

    def evaluate(self, record: Union[Dict, Any]) -> DecisionResult:

        record_data = self._normalize_record(record)

        record_id = record_data.get("record_id")

        if record_id is None:
            raise RuleEvaluationError(
                "record_id missing from record"
            )

        for rule in self.rules:

            matched = self._evaluate_rule(rule, record_data)

            decision: Optional[str] = None

            if matched:
                decision = rule.decision

            # Log once per rule
            self.audit_logger.log(
                record_id=record_id,
                rule_id=rule.rule_id,
                priority=rule.priority,
                matched=matched,
                decision=decision,
            )

            if matched and rule.stop_on_match:

                return DecisionResult(
                    decision=rule.decision,
                    rule_id=rule.rule_id,
                    reason=rule.reason,
                )

        raise RuleEvaluationError(
            f"No matching rule found for record {record_id}"
        )

    def _normalize_record(self, record) -> Dict[str, Any]:

        # Pydantic model
        if hasattr(record, "model_dump"):
            return record.model_dump()

        # Dict
        if isinstance(record, dict):
            return record

        raise RuleEvaluationError(
            f"Unsupported record type: {type(record)}"
        )

    def _evaluate_rule(
        self,
        rule: Rule,
        record_data: Dict[str, Any],
    ) -> bool:

        conditions = rule.conditions

        if conditions.all is not None:
            return self._eval_all(conditions.all, record_data)

        if conditions.any is not None:
            return self._eval_any(conditions.any, record_data)

        return False

    def _eval_all(
        self,
        conditions: List[Condition],
        record_data: Dict[str, Any],
    ) -> bool:

        if not conditions:
            return True

        for cond in conditions:
            if not self._eval_condition(cond, record_data):
                return False

        return True

    def _eval_any(
        self,
        conditions: List[Condition],
        record_data: Dict[str, Any],
    ) -> bool:

        if not conditions:
            return True

        for cond in conditions:
            if self._eval_condition(cond, record_data):
                return True

        return False

    def _eval_condition(
        self,
        cond: Condition,
        record_data: Dict[str, Any],
    ) -> bool:

        field = cond.field

        if field not in record_data:
            raise RuleEvaluationError(
                f"Unknown field '{field}' in rule"
            )

        record_value = record_data[field]

        operator = cond.operator

        if operator not in OPERATOR_MAP:
            raise RuleEvaluationError(
                f"Unsupported operator '{operator}'"
            )

        func = OPERATOR_MAP[operator]

        try:
            return func(record_value, cond.value)

        except Exception as e:

            raise RuleEvaluationError(
                f"Error evaluating condition on field '{field}': {e}"
            )