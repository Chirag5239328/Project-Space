from fastapi import APIRouter, UploadFile, File, HTTPException
from api.services.engine_service import save_uploaded_csv

router = APIRouter()


@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):

    try:
        csv_id, schema, metadata = save_uploaded_csv(file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "csv_id": csv_id,
        "schema": schema,
        "metadata": metadata
    }