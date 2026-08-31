from fastapi import APIRouter, HTTPException
from api.services.engine_service import save_rules_json

router = APIRouter()


@router.post("/rules")
async def save_rules(rules: dict):

    try:
        rules_id = save_rules_json(rules)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"rules_id": rules_id}