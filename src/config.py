from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

# Single Source of Truth

# ---------- OpenAI ----------

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = "gpt-4.1-mini"

# ---------- Database ----------

DATABASE_PATH = Path("data/customer360.db")