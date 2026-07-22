import logging

from exceptions import Customer360Error
from logging_config import configure_logging
from pipeline import ask_database

configure_logging()

logger = logging.getLogger(__name__)

question = "Show me the five customers with the highest lifetime value."

try:
    result = ask_database(question)

    print("\nGenerated SQL:")
    print(result.sql)

    print("\nQuery result:")
    print(result.data)

    print("\nAI answer:")
    print(result.answer)

except Customer360Error as error:
    logger.error("The analytics request failed: %s", error)

    print("\nUnable to answer the question:")
    print(error)