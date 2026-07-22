class Customer360Error(Exception):
    """
    Base exception for expected application errors.
    """

class LLMServiceError(Customer360Error):
    """
    Raised when the language-model service cannot complete a request.
    """

class QueryGenerationError(Customer360Error):
    """
    Raised when a safe SQL query cannot be generated.
    """

class DatabaseQueryError(Customer360Error):
    """
    Raised when the database cannot execute a query.
    """