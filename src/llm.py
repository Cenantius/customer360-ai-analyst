import os
from dotenv import load_dotenv
from openai import OpenAI
from config import MODEL_NAME
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_llm(prompt: str) -> str:
    """
    Sends a prompt to the OpenAI API and returns the model's text response.
    """

    response = client.responses.create(
        model=MODEL_NAME,
        input=prompt,
    )

    return response.output_text