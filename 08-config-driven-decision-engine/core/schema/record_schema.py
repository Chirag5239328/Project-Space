from pydantic import BaseModel, Field, field_validator


class Record(BaseModel):

    record_id: str = Field(..., min_length=1)
    age: int = Field(..., ge=18, le=100)
    annual_income: int = Field(..., gt=0)
    credit_score: int = Field(..., ge=300, le=900)
    country: str = Field(..., min_length=1)
    kyc_verified: bool
    requested_amount: int = Field(..., gt=0)
    employment_type: str

    @field_validator("record_id")
    @classmethod
    def validate_record_id(cls, v):
        if not v.strip():
            raise ValueError("record_id cannot be blank")
        return v

    @field_validator("country")
    @classmethod
    def validate_country(cls, v):
        if not v.strip():
            raise ValueError("country cannot be blank")
        return v

    @field_validator("employment_type")
    @classmethod
    def validate_employment_type(cls, v):
        allowed = {"salaried", "self_employed", "unemployed"}

        if v not in allowed:
            raise ValueError(
                f"employment_type must be one of {allowed}"
            )

        return v
