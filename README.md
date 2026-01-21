# Decision Intelligence API (ML + LLM)

A production-style AI engineering project that exposes machine learning and large language model (LLM) capabilities through a FastAPI service.

This system ingests raw CSV data, performs automated analysis and baseline machine learning, and generates structured, executive-ready insights using an LLM abstraction layer. The project is designed to demonstrate AI Engineering skills such as system design, ML pipelines, API development, and LLM integration — not just notebook-based experimentation.

---

## What This Project Does

Given a CSV file, the API automatically:

- Profiles the dataset (rows, columns, data types, missing values)
- Computes statistical summaries and correlations
- Performs anomaly detection when numeric data is available
- Trains a baseline ML model (classification or regression) if a target column is provided
- Evaluates the model using appropriate metrics
- Generates structured business insights using an LLM layer
- Returns results via a REST API using job-based execution

All outputs are returned as structured JSON, making them suitable for dashboards, reports, or downstream services.

---

## Why This Project

This project reflects how real-world AI systems are built and deployed:

- ML and analytics are exposed as services, not notebooks
- LLMs are used as an interpretation and decision layer
- Outputs are schema-driven and structured
- The system is modular, testable, and production-aware

---

## Tech Stack

- Python
- FastAPI + Uvicorn
- Pandas / NumPy
- Scikit-learn
- LLM abstraction layer (mocked for local development)

---

## Project Structure

decision-intelligence-api/
├── backend/
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── api/
│       ├── core/
│       ├── ingestion/
│       ├── analysis/
│       ├── ml/
│       └── llm/
├── README.md
└── .gitignore

---

## Requirements

- Python 3.10+ (recommended)
- pip
- Virtual environment support

---

## Setup & Run Instructions

### 1. Clone the Repository

git clone https://github.com/JALapon/decision-intelligence-api.git
cd decision-intelligence-api

---

### 2. Create and Activate a Virtual Environment

Windows (PowerShell)
python -m venv .venv
.venv\Scripts\activate

macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

---

### 3. Install Dependencies

pip install -r backend/requirements.txt

---

### 4. Start the API Server

Windows (PowerShell)
$env:PYTHONPATH="."
uvicorn backend.app.main:app

macOS / Linux
export PYTHONPATH="."
uvicorn backend.app.main:app

The API will be available at:
http://127.0.0.1:8000

---

### 5. Open Interactive API Documentation

http://127.0.0.1:8000/docs

---

## API Endpoints

### POST /analyze

Uploads a CSV file and starts analysis.

Optional parameters:
- target: column name used for ML training
- task: auto, classification, or regression

---

### GET /results/{job_id}

Fetches results after processing completes.

Returns:
- Data profile
- Statistical analysis
- Anomaly detection summary
- ML model metrics (if applicable)
- Structured LLM-generated insights

---

## LLM Behavior

The LLM layer runs in mock mode by default.

This allows:
- No API keys required
- Deterministic local development
- Easier testing and demos
- Clean separation between ML logic and language reasoning

---

## Stopping the Server

CTRL + C

---

## Future Enhancements

- Docker and docker-compose
- Persistent job storage (Redis/Postgres)
- Stronger models and cross-validation
- LLM provider integration and evaluation
- Monitoring and drift detection

---
