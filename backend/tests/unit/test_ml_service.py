from backend.src.services import ml_service
import pandas as pd


def test_linear_regression():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [2, 4, 6]})
    result = ml_service.run_ml_task("regression", df, "y", regression_type="linear")
    assert "metrics" in result
    assert "r2_score" in result["metrics"]


def test_decision_tree_regression():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [2, 4, 6]})
    result = ml_service.run_ml_task(
        "regression", df, "y", regression_type="decision_tree"
    )
    assert "metrics" in result
    assert "r2_score" in result["metrics"]


def test_decision_tree_classification():
    df = pd.DataFrame({"x": [1, 2, 3, 4], "y": [0, 1, 0, 1]})
    result = ml_service.run_ml_task("classification", df, "y")
    assert "metrics" in result
    assert "accuracy" in result["metrics"]
