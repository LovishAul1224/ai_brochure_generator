from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

# Default model
MODEL = os.getenv(
    "MODEL",
    "meta-llama/llama-3.3-70b-instruct"
)

# Application Settings
APP_NAME = "AI Brochure Generator"
MAX_CONTENT_LENGTH = 2000
REQUEST_TIMEOUT = 20