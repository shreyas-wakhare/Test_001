"""Structured application logging for DWEX Groundwater Modelling platform."""

from __future__ import annotations

import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

DEFAULT_LOG_FORMAT = "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

_configured = False


def setup_logger(
    name: str = "dwex",
    log_level: str | int | None = None,
    log_dir: Path | str | None = None,
    log_file: str = "dwex_groundwater.log",
    max_bytes: int = 10 * 1024 * 1024,  # 10 MB
    backup_count: int = 5,
) -> logging.Logger:
    """Configure and return a structured logger with console and rotating file handlers."""
    global _configured

    logger = logging.getLogger(name)

    if log_level is None:
        env_level = os.getenv("DWEX_LOG_LEVEL", "INFO").upper()
        level = getattr(logging, env_level, logging.INFO)
    elif isinstance(log_level, str):
        level = getattr(logging, log_level.upper(), logging.INFO)
    else:
        level = log_level

    logger.setLevel(level)

    # Avoid duplicate handlers on subsequent calls
    if logger.hasHandlers():
        return logger

    formatter = logging.Formatter(fmt=DEFAULT_LOG_FORMAT, datefmt=DATE_FORMAT)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File Handler
    if log_dir is None:
        # Default to project root logs/ directory
        project_root = Path(__file__).resolve().parent.parent.parent.parent
        resolved_log_dir = project_root / "logs"
    else:
        resolved_log_dir = Path(log_dir)

    resolved_log_dir.mkdir(parents=True, exist_ok=True)
    file_path = resolved_log_dir / log_file

    file_handler = RotatingFileHandler(
        file_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    _configured = True
    return logger


def get_logger(module_name: str | None = None) -> logging.Logger:
    """Obtain a scoped child logger under the DWEX logging namespace."""
    base_name = "dwex"
    if not logging.getLogger(base_name).hasHandlers():
        setup_logger(base_name)
    if module_name:
        return logging.getLogger(f"{base_name}.{module_name}")
    return logging.getLogger(base_name)
