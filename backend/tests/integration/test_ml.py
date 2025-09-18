import io
from fastapi.testclient import TestClient
from fastapi import FastAPI

try:
    from backend.src.api.ml import router as ml_router
except ImportError:
    ml_router = None

app = FastAPI()
if ml_router:
    app.include_router(ml_router)

client = TestClient(app)


def test_linear_regression():
    if not ml_router:
        assert False, "ML router not implemented yet"
    csv_content = "x,y\n1,2\n2,4\n3,6\n"
    response = client.post(
        "/ml",
        data={"task": "regression", "target": "y"},
        files={"file": ("data.csv", io.BytesIO(csv_content.encode()), "text/csv")},
    )
    assert response.status_code in (200, 501)
    if response.status_code == 200:
        data = response.json()
        assert "metrics" in data
        assert "r2_score" in data["metrics"]
        assert "plot" in data


def test_classification():
    if not ml_router:
        assert False, "ML router not implemented yet"
    csv_content = "x,y\n1,0\n2,1\n3,0\n4,1\n"
    response = client.post(
        "/ml",
        data={"task": "classification", "target": "y"},
        files={"file": ("data.csv", io.BytesIO(csv_content.encode()), "text/csv")},
    )
    assert response.status_code in (200, 501)
    if response.status_code == 200:
        data = response.json()
        assert "metrics" in data
        assert "accuracy" in data["metrics"]
        assert "plot" in data
