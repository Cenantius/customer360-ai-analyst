import logging

from llm import ask_llm
from prompts import DATABASE_SCHEMA
from database import get_database_schema


logger = logging.getLogger(__name__)

def generate_sql(question: str) -> str:
    """
    Generates a SQLite query from a natural-language question.
    """

    logger.info("Generating SQL query")

    database_schema = get_database_schema()

    prompt = f"""
You are a senior SQLite analyst.

Your task is to convert the user's question into a valid SQLite query.

Rules:
- Use only the tables, views, and columns described below.
- Never invent table names or column names.
- Prefer an existing analytics view when it directly answers the question.
- Return only the SQL query.
- Do not use Markdown code fences.
- Do not explain the query.
- Generate only read-only SELECT queries.

Database schema:
{database_schema}

User question:
{question}
"""
    generated_sql = ask_llm(prompt).strip()

    logger.info("SQL query generated succesfully")

    return generated_sql