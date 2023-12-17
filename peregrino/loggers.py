from loguru import logger

from .config import LOG_PATH

logger.add(
    LOG_PATH,
    level='DEBUG',
    format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}',
    rotation='500 MB',
    serialize=True,
    backtrace=True,
    diagnose=True,
    enqueue=True,
)
