from typing import Dict, List


class RuleMetadataError(Exception):
    pass


# Operators allowed per type
OPERATOR_REGISTRY = {
    "int": ["<", "<=", ">", ">=", "==", "!=", "between"],
    "float": ["<", "<=", ">", ">=", "==", "!=", "between"],
    "str": ["==", "!=", "in", "not_in"],
    "bool": ["==", "!="],
}


class RuleMetadataService:

    def __init__(self, schema: Dict[str, dict]):
        self.schema = schema

    def get_fields(self) -> List[str]:
        return list(self.schema.keys())

    def get_allowed_operators(self) -> Dict[str, List[str]]:

        result = {}

        for field, meta in self.schema.items():

            field_type = meta["type"]

            if field_type not in OPERATOR_REGISTRY:
                raise RuleMetadataError(
                    f"No operators for type {field_type}"
                )

            result[field] = OPERATOR_REGISTRY[field_type]

        return result

    def describe(self) -> Dict:

        return {
            "fields": self.get_fields(),
            "operators": self.get_allowed_operators(),
            "types": {
                f: meta["type"]
                for f, meta in self.schema.items()
            },
        }
