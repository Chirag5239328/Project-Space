from typing import List, Dict

from core.rules.rule_schema import RuleSet, Rule, Condition, ConditionGroup


class RuleAdapterError(Exception):
    pass


class RuleAdapter:

    def adapt(self, json_rules: List[Dict]) -> RuleSet:

        rules = []

        for r in json_rules:

            rule = self._convert_rule(r)

            rules.append(rule)

        return RuleSet(rules=rules)

    def _convert_rule(self, r: Dict) -> Rule:

        try:

            conditions = self._build_conditions(r["conditions"])

            return Rule(
                rule_id=r["rule_id"],
                priority=r["priority"],
                decision=r["decision"],
                stop_on_match=r["stop_on_match"],
                reason=r["reason"],
                conditions=conditions,
            )

        except KeyError as e:
            raise RuleAdapterError(
                f"Missing field: {e}"
            )

    def _build_conditions(self, conds: List[Dict]) -> ConditionGroup:

        # Default rule
        if not conds:
            return ConditionGroup(all=[])

        conditions = []

        for c in conds:

            cond = Condition(
                field=c["field"],
                operator=c["operator"],
                value=c["value"],
            )

            conditions.append(cond)

        # For v2 we use AND only (all)
        return ConditionGroup(all=conditions)
