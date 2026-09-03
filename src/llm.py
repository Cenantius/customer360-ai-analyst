import logging

import openai
from openai import OpenAI

from config import MODEL_NAME, OPENAI_API_KEY
from exceptions import LLMServiceError


logger = logging.getLogger(__name__)


def ask_llm(prompt: str) -> str:
    """
    Sends a prompt to the OpenAI API and returns the model's text response.
    """
    logger.info("Sending request to OpenAI API")

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)

        response = client.responses.create(
            model=MODEL_NAME,
            input=prompt,
        )

    except openai.APIConnectionError as error:
        logger.exception("Could not connect to OpenAI API")
        raise LLMServiceError(
            "The AI service could not be reached."
        ) from error

    except openai.RateLimitError as error:
        logger.exception("OpenAI API rate limit or quota was exceeded")
        raise LLMServiceError(
            "The AI service usage limit was reached."
        ) from error

    except openai.APIStatusError as error:
        logger.exception(
            "OpenAI API returned status code %s",
            error.status_code,
        )
        raise LLMServiceError(
            "The AI service returned an unexpected error."
        ) from error

    logger.info("Received response from OpenAI API")

    return response.output_text