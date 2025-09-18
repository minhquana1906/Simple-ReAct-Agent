from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import pandas as pd
from backend.src.services.ml_service import run_ml_task

router = APIRouter()


@router.post("/ml")
async def ml_task(
    file: UploadFile = File(...),
    task: str = Form(...),
    target: str = Form(...),
    regression_type: str = Form("linear"),
):
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")
    df = pd.read_csv(file.file)
    try:
        result = run_ml_task(task, df, target, regression_type=regression_type)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result
