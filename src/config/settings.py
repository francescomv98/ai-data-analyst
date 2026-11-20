from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    app_name: str = "AI Data Analyst"
    app_version: str = "1.0.0"
    openai_api_key: str
    chat_model: str = "gpt-4.1-mini"
    upload_directory: str = "data/uploads"
    log_directory: str = "logs"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8"
    )

settings = Settings()