from typing import Any

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

from exceptions import Customer360Error
from pipeline import ask_database


app = FastAPI(
    title="Customer360 AI Analyst API",
    version="0.1.0",
)

def get_analytics_pipeline():
    return ask_database

class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    question: str
    answer: str
    sql: str
    execution_time: float
    data: list[dict[str, Any]]

## when the server gets an HTTP GET into /health, run a health_check()
@app.get("/health")
def health_check() -> dict:
    return {
        "status": "ok",
    }

@app.post("/ask", response_model=AskResponse)
def ask(
    request: AskRequest,
    ## give analytics_pipeline -parameter the dependency,
    ## that get_analytics_pipeline() produces
    analytics_pipeline=Depends(get_analytics_pipeline)
) -> AskResponse:
    try:
        result = analytics_pipeline(request.question)

        return AskResponse(
            question=result.question,
            answer=result.answer,
            sql=result.sql,
            execution_time=result.execution_time,
            data=result.data.to_dict(orient="records"),
        )

    except Customer360Error as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        ) from error