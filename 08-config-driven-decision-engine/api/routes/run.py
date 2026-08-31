from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from api.services.engine_service import execute_engine


router = APIRouter()


class RunRequest(BaseModel):
    csv_id: str
    rules_id: str


@router.post("/run")
async def run_engine_endpoint(req: RunRequest):

    try:
        run_id, run_dir = execute_engine(req.csv_id, req.rules_id)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "run_id": run_id,
        "output_dir": str(run_dir)
    }