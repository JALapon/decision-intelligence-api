import uuid
from fastapi import APIRouter, UploadFile, File, Form, BackgroundTasks
from backend.app.core.job_store import job_store
from backend.app.ingestion.load_data import load_csv_to_df
from backend.app.analysis.stats import run_stats_analysis
from backend.app.analysis.anomalies import run_anomaly_detection
from backend.app.ml.model import run_baseline_model
from backend.app.llm.client import generate_llm_insights

# Define the API router
router = APIRouter()

# Endpoint to upload a file and start analysis
@router.post("/analyze")
async def analyze(background_tasks: BackgroundTasks, file: UploadFile = File(...), target: str = Form(None), task: str = Form("auto")):
    job_id = str(uuid.uuid4())
    job_store.create(job_id)
    content = await file.read()
    background_tasks.add_task(run_job, job_id, content, target, task)
    return {"job_id": job_id, "status": "queued"}

# Endpoint to check job status and get results
@router.get("/results/{job_id}")
def results(job_id: str):
    return job_store.get(job_id)

# Function to run the analysis job
def run_job(job_id, content, target, task):
    df, profile = load_csv_to_df(content)
    stats = run_stats_analysis(df)
    anomalies = run_anomaly_detection(df)
    ml = run_baseline_model(df, target, task)
    llm = generate_llm_insights(profile, stats, ml)
    job_store.update(job_id, "completed", result={"profile": profile, "stats": stats, "anomalies": anomalies, "ml": ml, "llm": llm})
