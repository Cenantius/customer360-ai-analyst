from logging_config import configure_logging
from pipeline import ask_database

configure_logging()

question = "Show me the five customers with the highest lifetime value."

result = ask_database(question)

print("\nGenerated SQL:")
print(result.sql)

print("\nQuery result:")
print(result.data)

print("\nAI answer:")
print(result.answer)