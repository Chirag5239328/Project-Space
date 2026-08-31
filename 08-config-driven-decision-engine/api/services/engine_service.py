from pathlib import Path
import uuid
import json
import shutil

from fastapi import UploadFile

from core.schema.schema_inferer import SchemaInferer
from core.rules.rule_metadata import RuleMetadataService
from run_engine import run_engine


UPLOAD_DIR = Path("api_storage/uploads")
RULES_DIR = Path("api_storage/rules")
RUNS_DIR = Path("api_storage/runs")

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
RULES_DIR.mkdir(parents=True, exist_ok=True)
RUNS_DIR.mkdir(parents=True, exist_ok=True)


def save_uploaded_csv(file: UploadFile):

    file_id = str(uuid.uuid4())
    file_path = UPLOAD_DIR / f"{file_id}.csv"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    inferer = SchemaInferer()
    schema = inferer.infer(str(file_path))

    metadata = RuleMetadataService(schema).describe()

    return file_id, schema, metadata


def save_rules_json(rules: dict):

    rules_id = str(uuid.uuid4())
    rules_path = RULES_DIR / f"{rules_id}.json"

    with open(rules_path, "w", encoding="utf-8") as f:
        json.dump(rules, f, indent=2)

    return rules_id


def execute_engine(csv_id: str, rules_id: str):

    csv_path = UPLOAD_DIR / f"{csv_id}.csv"
    rules_path = RULES_DIR / f"{rules_id}.json"

    if not csv_path.exists():
        raise FileNotFoundError("CSV not found")

    if not rules_path.exists():
        raise FileNotFoundError("Rules not found")

    run_id = str(uuid.uuid4())

    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    run_engine(
        str(csv_path),
        str(rules_path),
        str(run_dir)
    )

    return run_id, run_dir


def fetch_results(run_id: str):

    run_dir = RUNS_DIR / run_id

    if not run_dir.exists():
        raise FileNotFoundError("Run not found")

    files = [f.name for f in run_dir.iterdir()]

    return files