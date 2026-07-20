import logging
from pathlib import Path
from src.config.settings import settings

log_dir = Path(settings.log_directory)
log_dir.mkdir(parents=True, exist_ok=True)

log_file = log_dir / "app.log"

logger = logging.getLogger(settings.app_name)

if not logger.handlers:
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)