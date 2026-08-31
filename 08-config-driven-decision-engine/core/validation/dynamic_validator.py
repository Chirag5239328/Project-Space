from typing import Optional, Dict, Any, Type

from pydantic import BaseModel, create_model, ValidationError


class DynamicValidationError(Exception):
    pass


TYPE_MAP = {
    "int": int,
    "float": float,
    "bool": bool,
    "str": str,
}


class DynamicValidator:

    def __init__(self, schema: Dict[str, dict]):
        self.schema = schema
        self.model = self._build_model()

    def _build_model(self) -> Type[BaseModel]:

        fields = {}

        for name, meta in self.schema.items():

            t = meta["type"]

            if t not in TYPE_MAP:
                raise DynamicValidationError(
                    f"Unsupported type: {t}"
                )

            py_type = TYPE_MAP[t]

            if meta.get("nullable", False):
                py_type = Optional[py_type]

            default = None if meta.get("nullable", False) else ...

            fields[name] = (py_type, default)

        return create_model("DynamicRecord", **fields)

    def validate(self, row: Dict[str, Any]) -> BaseModel:

        try:
            return self.model(**row)

        except ValidationError as e:
            raise DynamicValidationError(str(e))
