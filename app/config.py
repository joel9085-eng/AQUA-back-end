import os
from dotenv import load_dotenv

load_dotenv()

# Minimal settings using environment variables to avoid pydantic BaseSettings migration issues
class Settings:
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "True").lower() in ("1", "true", "yes")


settings = Settings()

# Use environment variable for sensitive API keys; do not commit real keys.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
