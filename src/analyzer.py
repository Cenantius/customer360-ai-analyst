import logging

from llm import ask_llm


logger = logging.getLogger(__name__)

def analyze_results(
    question: str,
    results: str,
    sql: str = "",
) -> str:
    """
    Converts SQL query results into a clear natural-language answer.
    """

    logger.info("Generating natural-language analysis")

    prompt = f"""
You are a business data analyst.

Answer the user's question using only the query results provided below.

Rules:
- Use the query results as the source of factual data.
- Use the SQL query only to understand how the result rows were selected,
  filtered, sorted, grouped, or limited.
- Do not invent information.
- Do not mention SQL or the database unless necessary.
- Be concise and clear.
- Include relevant numbers.
- If the results are empty, say that no matching data was found.
- If the SQL intentionally selects a ranked row using ORDER BY, LIMIT,
  or OFFSET, interpret that ranking when answering the user's question.

User question:
{question}

SQL used to produce the results:
{sql}

Query results:
{results}
"""
    
    answer = ask_llm(prompt).strip()

    logger.info("Natural-language analysis generated succesfully")

    return answer