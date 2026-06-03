import sys
from loguru import logger

def setup_logging(level: str = "INFO"):
    """Setup global logger format and sinks"""
    logger.remove()
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level=level,
        enqueue=True,
    )

def get_logger(name: str):
    """Get a contextual logger."""
    return logger.bind(name=name)
