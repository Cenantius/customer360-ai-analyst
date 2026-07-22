from pathlib import Path
from config import DATABASE_PATH
from exceptions import DatabaseQueryError
import sqlite3
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def create_read_only_connection() -> sqlite3.Connection:
    """
    Opens the Customer360 SQLite database in read-only mode.
    """

    # ro = read only
    database_uri = DATABASE_PATH.resolve().as_uri() + "?mode=ro"

    return sqlite3.connect(
        database_uri,
        uri=True,
    )

def run_query(query: str) -> pd.DataFrame:
    """
    Runs a read-only SQL query and returns the result as a DataFrame.
    """

    logger.info("Executing read-only SQL query")

    connection = create_read_only_connection()

    try:
        result = pd.read_sql_query(query, connection)
    except (sqlite3.Error, pd.errors.DatabaseError) as error:
        logger.exception("Database query failed")

        raise DatabaseQueryError(
            "The database could not execute the generated query."
        ) from error
    finally:
        connection.close()

    logger.info(
        "SQL query completed successfully with %s rows",
        len(result),
    )

    return result

def get_database_schema() -> str:
    """
    Reads tables, views, and their columns from the SQLite database and returns a text description
    suitable for an LLM prompt.
    """

    logger.info("Reading database schema")

    connection = create_read_only_connection()

    try:
        objects = connection.execute(
            """
            SELECT name, type
            FROM sqlite_master
            WHERE type IN ('table', 'view')
                AND name NOT LIKE 'sqlite_%'
            ORDER BY type, name;
            """
        ).fetchall()

        schema_sections = []

        for object_name, object_type in objects:
            columns = connection.execute(
                f'PRAGMA table_info("{object_name}");'
            ).fetchall()

            column_lines = []

            for column in columns:
                column_name = column[1]
                column_type = column[2] or "UNKNOWN"
                column_lines.append(
                    f"- {column_name}: {column_type}"
                )

            section = (
                f"{object_type.upper()}: {object_name}\n"
                + "\n".join(column_lines)
            )

            schema_sections.append(section)

        logger.info(
            "Database schema loaded with %s objects",
            len(schema_sections),
        )

        return "\n\n".join(schema_sections)
    
    finally:
        connection.close()