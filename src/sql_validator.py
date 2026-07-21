def validate_sql(query: str) -> str:
    """
    Validates that the generated SQL is a single read-only SELECT query.

    Returns the cleaned query if it is accepted.
    Raises ValueError if the query is unsafe.
    """

    cleaned_query = query.strip()

    if not cleaned_query:
        raise ValueError("The generated SQL query is empty.")
    
    normalized_query = cleaned_query.upper()

    if not normalized_query.startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed.")
    
    forbidden_keywords = (
        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "ALTER",
        "CREATE",
        "REPLACE",
        "TRUNCATE",
        "ATTACH",
        "DETACH",
        "PRAGMA",
    )

    for keyword in forbidden_keywords:
        if keyword in normalized_query:
            raise ValueError(
                f"Unsafe SQL detected: keyword '{keyword}' is not allowed."
            )
        
    query_without_final_semicolon = cleaned_query.rstrip(";")

    if ";" in query_without_final_semicolon:
        raise ValueError("Only one SQL statement is allowed.")
    
    return cleaned_query