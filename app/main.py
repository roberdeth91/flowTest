# app/main.py
from fastapi import FastAPI

app = FastAPI()
tasks = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def list_tasks():
    return tasks

@app.post("/tasks")
def create_task(title: str):
    task = {"id": len(tasks) + 1, "title": title}
    tasks.append(task)
    return task
