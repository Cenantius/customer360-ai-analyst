from analyzer import analyze_results
from database import run_query
from sql_generator import generate_sql
from sql_validator import validate_sql
from logging_config import configure_logging

configure_logging()

question = "Show me the five customers with the highest lifetime value."

generated_sql = generate_sql(question)
safe_sql = validate_sql(generated_sql)

print("Generated SQL:")
print(safe_sql)

result = run_query(safe_sql)

print("\nQuery result:")
print(result)

answer = analyze_results(
    question=question,
    results=result.to_string(index=False),
)

print("\nAI answer:")
print(answer)
