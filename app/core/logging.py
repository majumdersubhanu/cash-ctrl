import sys
from loguru import logger
from app.core.config import settings

def setup_logging():
    # Remove default handler
    logger.remove()

    # Define log format based on environment
    if settings.ENVIRONMENT == "prod":
        # Structured JSON logging for production
        logger.add(
            sys.stdout,
            format="{message}",
            serialize=True,
