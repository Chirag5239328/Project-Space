from pydantic import BaseModel, Field, field_validator, model_validator
from typing import List, Literal, Optional, Union


DecisionType = Literal["accept", "reject", "review"]
OperatorType = Literal["==", "!=", "<", "<=", ">", ">=", "between", "in"]


class Condition(BaseModel):
    field: str = Field(..., min_length=1)
    operator: OperatorType
    value: Union[int, str, bool, List[Union[int, str]]]

    @field_validator("value")
    @classmethod
    def validate_value(cls, v, info):
        operator = info.data.get("operator")

        if operator == "between":
            if not isinstance(v, list) or len(v) != 2:
                raise ValueError("between operator requires a list of exactly two values")
            if v[0] > v[1]:
                raise ValueError("between range must be [min, max]")

        if operator == "in":
            if not isinstance(v, list) or len(v) == 0:
                raise ValueError("in operator requires a non-empty list")

        return v


class ConditionGroup(BaseModel):
    all: Optional[List[Condition]] = None
    any: Optional[List[Condition]] = None

    @model_validator(mode="after")
    def validate_condition_group(self):
        if self.all is None and self.any is None:
            raise ValueError("Either 'all' or 'any' conditions must be provided")
        return self



class Rule(BaseModel):
    rule_id: str = Field(..., min_length=1)
    priority: int = Field(..., ge=1)
    decision: DecisionType
    stop_on_match: bool
    reason: str = Field(..., min_length=1)
    conditions: ConditionGroup


class RuleSet(BaseModel):
    rules: List[Rule]

    @model_validator(mode="after")
    def validate_ruleset(self):
        if not self.rules:
            raise ValueError("At least one rule must be defined")

        rule_ids = set()
        priorities = set()
        has_default_rule = False

        for rule in self.rules:
            if rule.rule_id in rule_ids:
                raise ValueError(f"Duplicate rule_id found: {rule.rule_id}")
            rule_ids.add(rule.rule_id)

            if rule.priority in priorities:
                raise ValueError(f"Duplicate priority found: {rule.priority}")
            priorities.add(rule.priority)

            if rule.conditions.all == [] or rule.conditions.any == []:
                has_default_rule = True

        if not has_default_rule:
            raise ValueError("A default rule with empty conditions must be defined")

        return self
