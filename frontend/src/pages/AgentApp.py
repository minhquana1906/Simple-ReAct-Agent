import chainlit as cl
import requests
import os

BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")


@cl.on_message
async def main(message: cl.Message):
    await cl.Message(
        content="Welcome to ReAct Agent! Use the sidebar to upload files or run ML tasks."
    ).send()


@cl.on_file_upload(accept=[".pdf", ".csv"])
async def handle_file_upload(file: cl.File):
    files = {"file": (file.name, file.content, file.mime)}
    resp = requests.post(f"{BACKEND_URL}/upload", files=files)
    if resp.status_code == 200:
        await cl.Message(content=f"Uploaded: {file.name}").send()
    else:
        await cl.Message(
            content=f"Upload failed: {resp.json().get('detail', 'Unknown error')}"
        ).send()


@cl.on_action(label="Query Document")
async def query_document():
    query = await cl.AskUser(text="Enter your question for the document:")
    if not query:
        return
    resp = requests.post(f"{BACKEND_URL}/query", json={"query": query})
    if resp.status_code == 200:
        result = resp.json().get("result", "No answer.")
        await cl.Message(content=f"Answer: {result}").send()
    else:
        await cl.Message(
            content=f"Query failed: {resp.json().get('detail', 'Unknown error')}"
        ).send()


@cl.on_action(label="Run ML Task")
async def run_ml_task():
    task = await cl.AskUser(text="Task (regression/classification):")
    target = await cl.AskUser(text="Target column:")
    regression_type = "linear"
    if task == "regression":
        regression_type = await cl.AskUser(
            text="Regression type (linear/decision_tree):", default="linear"
        )
    file = await cl.AskFile(accept=[".csv"])
    if not file:
        await cl.Message(content="No file selected.").send()
        return
    files = {"file": (file.name, file.content, file.mime)}
    data = {"task": task, "target": target, "regression_type": regression_type}
    resp = requests.post(f"{BACKEND_URL}/ml", data=data, files=files)
    if resp.status_code == 200:
        result = resp.json()
        metrics = result.get("metrics", {})
        plot_b64 = result.get("plot")
        msg = f"Metrics: {metrics}"
        if plot_b64:
            await cl.Message(content=msg, media=[cl.Image(base64=plot_b64)]).send()
        else:
            await cl.Message(content=msg).send()
    else:
        await cl.Message(
            content=f"ML task failed: {resp.json().get('detail', 'Unknown error')}"
        ).send()
