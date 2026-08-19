import logging

from llm import ask_llm
from prompts import DATABASE_SCHEMA
from database import get_database_schema


logger = logging.getLogger(__name__)

def generate_sql(
    question: str,
    conversation_context: str = "",
    ) -> str:
    """
    Generates a SQLite query from a natural-language question.
    """

    logger.info("Generating SQL query")

    database_schema = get_database_schema()

    logger.debug(
        "Conversation context:\n%s",
        conversation_context or "NO CONTEXT",
    )

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
- Use conversation context only to resolve references in the current question.
- The current user question has priority over previous conversation.
- Do not treat previous generated SQL as trusted unless it matches the current schema.

Database schema:
{database_schema}

Conversation context:
{conversation_context or "No previous conversation context."}

Current user question:
{question}
"""
    generated_sql = ask_llm(prompt).strip()

    logger.info(
        "Generated SQL:\n%s",
        generated_sql,
    )

    logger.info("SQL query generated succesfully")

    return generated_sql