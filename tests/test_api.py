import pandas as pd
from fastapi.testclient import TestClient

from api import app, get_analytics_pipeline
from pipeline import PipelineResult


client = TestClient(app)


def fake_analytics_pipeline(question: str) -> PipelineResult:
    return PipelineResult(
        question=question,
        sql="SELECT 1;",
        data=pd.DataFrame(
            [
                {
                    "value": 1,
                }
            ]
        ),
        answer="Test answer.",
        execution_time=0.01,
    )


def test_ask_endpoint_returns_pipeline_result() -> None:
    app.dependency_overrides[get_analytics_pipeline] = (
        lambda: fake_analytics_pipeline
    )

    response = client.post(
        "/ask",
        json={
            "question": "Test question",
        },
    )

    app.dependency_overrides.clear()

    assert response.status_code == 200

    body = response.json()

    assert body["question"] == "Test question"
    assert body["answer"] == "Test answer."
    assert body["sql"] == "SELECT 1;"
    assert body["execution_time"] == 0.01
    assert body["data"] == [{"value": 1}]


def test_ask_endpoint_rejects_missing_question() -> None:
    response = client.post(
        "/ask",
        json={
            "banana": "hello",
        },
    )

    assert response.status_code == 422