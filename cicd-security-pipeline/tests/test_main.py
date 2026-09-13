import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.main import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_add_todo():
    client = app.test_client()
    response = client.post("/todos", json={"task": "learn CI/CD"})
    assert response.status_code == 201
    assert response.get_json()["task"] == "learn CI/CD"


def test_add_todo_missing_field():
    client = app.test_client()
    response = client.post("/todos", json={})
    assert response.status_code == 400
