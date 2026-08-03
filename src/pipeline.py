import logging
import time
from collections.abc import Callable
from dataclasses import dataclass

import pandas as pd

from analyzer import analyze_results
from database import run_query
from sql_generator import generate_sql
from sql_validator import validate_sql


logger = logging.getLogger(__name__)


SqlGenerator = Callable[[str], str]
SqlValidator = Callable[[str], str]
QueryRunner = Callable[[str], pd.DataFrame]
ResultAnalyzer = Callable[[str, str], str]


@dataclass
class PipelineResult:
    """
    Contains the complete result of an analytics pipeline run.
    """

    question: str
    sql: str
    data: pd.DataFrame
    answer: str

def ask_database(
    question: str,
    *,
    sql_generator: SqlGenerator = generate_sql,
    sql_validator: SqlValidator = validate_sql,
    query_runner: QueryRunner = run_query,
    result_analyzer: ResultAnalyzer = analyze_results,
) -> PipelineResult:
    """
    Runs the complete natural-language analytics pipeline

    Dependencies can be replaced for testing or alternative implementations.
    """

    start_time = time.perf_counter()

    logger.info("Starting analytics pipeline")

    sql_start = time.perf_counter()

    generated_sql = sql_generator(question)

    logger.info(
        "SQL generation took %.2f seconds",
        time.perf_counter() - sql_start,
    )

    safe_sql = sql_validator(generated_sql)

    db_start = time.perf_counter()

    data = query_runner(safe_sql)

    logger.info(
        "Database query took %.2f seconds",
        time.perf_counter() - db_start,
    )

    analyzing_start = time.perf_counter()

    answer = result_analyzer(
        question=question,
        results=data.to_string(index=False),
    )

    logger.info(
        "Result analysis took %.2f seconds",
        time.perf_counter() - analyzing_start, 
    )

    elapsed_time = time.perf_counter() - start_time

    logger.info(
        "Analytics pipeline completed successfully in %.2f seconds",
        elapsed_time,
    )

    return PipelineResult(
        question=question,
        sql=safe_sql,
        data=data,
        answer=answer,
    )