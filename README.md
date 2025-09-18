# Quickstart: Simple ReAct Agent

## 1. Prerequisites
- Python 3.11+
- Docker (for Qdrant vector DB)
- [uv](https://github.com/astral-sh/uv) (Python package manager)

## 2. Setup

### Backend
```bash
cd backend
uv venv
uv pip install -r pyproject.toml
```

### Frontend
```bash
cd frontend
uv venv
uv pip install -r pyproject.toml
```

### Start Qdrant (Vector DB)
```bash
docker-compose up -d qdrant
```

## 3. Running the App

### Start Backend (FastAPI)
```bash
cd backend
uvicorn src.api.upload:app --reload  # or your main app entrypoint
```

### Start Frontend (Chainlit)
```bash
cd frontend
chainlit run src/pages/AgentApp.py
```

## 4. Usage
- Upload PDF/CSV files via the UI
- Query documents (RAG)
- Run ML tasks (regression/classification, select regression type)

## 5. Testing
```bash
cd backend
pytest
```

---
For more details, see the `tasks.md` and code comments.
