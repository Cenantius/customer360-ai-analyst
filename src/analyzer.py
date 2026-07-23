import logging

from llm import ask_llm


logger = logging.getLogger(__name__)

def analyze_results(question: str, results: str) -> str:
    """
    Converts SQL query results into a clear natural-language answer.
    """

    logger.info("Generating natural-language analysis")

    prompt = f"""
You are a business data analyst.

Answer the user's question using only the query results provided below.

Rules:
- Do not invent information.
- Do not mention SQL or the database unless necessary.
- Be concise and clear.
- Include relevant numbers.
- If the results are empty, say that no matching data was found.

User question:
{question}

Query results:
{results}
"""
    
    answer = ask_llm(prompt).strip()

    logger.info("Natural-language analysis generated succesfully")

    return answer