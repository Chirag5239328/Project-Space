from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path

router = APIRouter()

RUNS_DIR = Path("api_storage/runs")


@router.get("/results/{run_id}")
def get_results(run_id: str):

    run_dir = RUNS_DIR / run_id

    if not run_dir.exists():
        raise HTTPException(status_code=404, detail="Run not found")

    files = [f.name for f in run_dir.iterdir()]

    return {
        "run_id": run_id,
        "files": files
    }


@router.get("/results/{run_id}/download/{filename}")
def download_file(run_id: str, filename: str):

    file_path = RUNS_DIR / run_id / filename

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="application/octet-stream"
    )