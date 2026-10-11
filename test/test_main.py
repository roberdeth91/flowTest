# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_create_task():
    r = client.post("/tasks", params={"title": "aprender actions"})
    assert r.status_code == 200
    assert r.json()["title"] == "aprender actions"
