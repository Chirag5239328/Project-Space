from typing import Any, List


def op_eq(a: Any, b: Any) -> bool:
    return a == b


def op_neq(a: Any, b: Any) -> bool:
    return a != b


def op_lt(a: Any, b: Any) -> bool:
    return a < b


def op_lte(a: Any, b: Any) -> bool:
    return a <= b


def op_gt(a: Any, b: Any) -> bool:
    return a > b


def op_gte(a: Any, b: Any) -> bool:
    return a >= b


def op_between(a: Any, bounds: List[Any]) -> bool:
    low, high = bounds
    return low <= a <= high


def op_in(a: Any, values: List[Any]) -> bool:
    return a in values


OPERATOR_MAP = {
    "==": op_eq,
    "!=": op_neq,
    "<": op_lt,
    "<=": op_lte,
    ">": op_gt,
    ">=": op_gte,
    "between": op_between,
    "in": op_in,
}
