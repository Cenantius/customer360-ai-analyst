import logging
from dataclasses import dataclass

import pandas as pd

from analyzer import analyze_results
from database import run_query
from sql_generator import generate_sql
from sql_validator import validate_sql

logger = logging.getLogger(__name__)

@dataclass
class PipelineResult:
    """
    Contains the complete result of an analytics pipeline run.
    """

    question: str
    sql: str
    data: pd.DataFrame
    answer: str

def ask_database(question: str) -> PipelineResult:
    """
    Runs the complete natural-language analytics pipeline
    """

    logger.info("Starting analytics pipeline")

    generated_sql = generate_sql(question)
    safe_sql = validate_sql(generated_sql)
    data = run_query(safe_sql)

    answer = analyze_results(
        question=question,
        results=data.to_string(index=False),
    )

    logger.info("Analytics pipeline completed succesfully")

    return PipelineResult(
        question=question,
        sql=safe_sql,
        data=data,
        answer=answer,
    )