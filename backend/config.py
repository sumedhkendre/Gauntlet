import os

from dotenv import load_dotenv


load_dotenv()


OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)

TARGET_MODEL = os.getenv(
    "TARGET_MODEL",
    "llama3.2"
)

JUDGE_MODEL = os.getenv(
    "JUDGE_MODEL",
    "llama3.2"
)

DATABASE_NAME = os.getenv(
    "DATABASE_NAME",
    "gauntlet.db"
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)