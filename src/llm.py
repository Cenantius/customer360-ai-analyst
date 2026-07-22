import os
import logging
from dotenv import load_dotenv
from openai import OpenAI
from config import MODEL_NAME
from config import OPENAI_API_KEY

logger = logging.getLogger(__name__)

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_llm(prompt: str) -> str:
    """
    Sends a prompt to the OpenAI API and returns the model's text response.
    """

    logger.info("Sending request to OpenAI API")

    response = client.responses.create(
        model=MODEL_NAME,
        input=prompt,
    )

    logger.info("Received response from OpenAI API")

    return response.output_text