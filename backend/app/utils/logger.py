import os
from loguru import logger
from app.config.settings import settings

os.makedirs(
    settings.LOG_PATH,
    exist_ok=True
)
logger.remove()

logger.add(
    sink=lambda msg:print(msg,end=""),
    level=settings.LOG_LEVEL,
    colorize=True
)

logger.add(
    settings.LOG_PATH/"resumeiq.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level=settings.LOG_LEVEL,
    enqueue=True
)

__all__=["logger"]