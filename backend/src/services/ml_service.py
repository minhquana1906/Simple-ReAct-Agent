import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.metrics import r2_score, accuracy_score
import matplotlib.pyplot as plt
import io
import base64


SUPPORTED_TASKS = ["regression", "classification"]
SUPPORTED_REGRESSION_TYPES = ["linear", "decision_tree"]


def run_ml_task(
    task: str, df: pd.DataFrame, target: str, regression_type: str = "linear"
):
    if task not in SUPPORTED_TASKS:
        raise ValueError(f"Unsupported task: {task}")
    X = df.drop(columns=[target])
    y = df[target]
    if task == "regression":
        if regression_type == "decision_tree":
            model = DecisionTreeRegressor()
            title = "Decision Tree Regression"
        else:
            model = LinearRegression()
            title = "Linear Regression"
        model.fit(X, y)
        y_pred = model.predict(X)
        metrics = {"r2_score": r2_score(y, y_pred)}
        plt.figure()
        plt.scatter(X.iloc[:, 0], y, label="True")
        plt.scatter(X.iloc[:, 0], y_pred, color="red", label="Predicted")
        plt.legend()
        plt.title(title)
    elif task == "classification":
        model = DecisionTreeClassifier()
        model.fit(X, y)
        y_pred = model.predict(X)
        metrics = {"accuracy": accuracy_score(y, y_pred)}
        plt.figure()
        plt.scatter(X.iloc[:, 0], y, label="True")
        plt.scatter(X.iloc[:, 0], y_pred, marker="x", color="red", label="Predicted")
        plt.legend()
        plt.title("Decision Tree Classification")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    plot_b64 = base64.b64encode(buf.read()).decode()
    return {"metrics": metrics, "plot": plot_b64}
