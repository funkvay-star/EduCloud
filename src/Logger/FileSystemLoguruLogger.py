from loguru import logger
import os
import sys
from src.helperModules.definitions import MB
from src.Logger.Logger import Logger


class FileSystemLoguruLogger(Logger):
    FILE_SYSTEM_LOGGER_FILE_SIZE = 500 * MB

    def __init__(self):
        log_dir = os.getenv('LOG_DIR', '/usr/src/app/logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self._log_path = os.path.join(log_dir, "application.log")
        print(f"Log path: {self._log_path}")

        # Remove any default handlers
        logger.remove()

        # Standard logging configuration
        logger.add(
            sys.stderr,
            level="DEBUG",
            format="<green>{time}</green> <level>{level}</level> "
                   "<cyan>{name}</cyan>:<cyan>{function}</cyan>:"
                   "<cyan>{line}</cyan> - <level>{message}</level>",
            filter=lambda record: not record["extra"].get("metadata_block", False)
        )
        logger.add(
            self._log_path,
            format="<green>{time}</green> <level>{level}</level> "
                   "<cyan>{name}</cyan>:<cyan>{function}</cyan>:"
                   "<cyan>{line}</cyan> - <level>{message}</level>",
            filter=lambda record: not record["extra"].get("metadata_block", False),
            rotation=self._rotate_logs,
            retention="10 days"
        )

        # Special handler for metadata block
        logger.add(
            sys.stderr,
            level="DEBUG",
            format="{message}",
            filter=lambda record: record["extra"].get("metadata_block", False)
        )
        logger.add(
            self._log_path,
            format="{message}",
            filter=lambda record: record["extra"].get("metadata_block", False),
            rotation=self._rotate_logs,
            retention="10 days"
        )

        logger.info(f"Logger initialized. Log path: {self._log_path}")

    def log_error(self, error: Exception):
        logger.error(error)

    def log_warning(self, message):
        logger.warning(message)

    def log_info(self, message, **kwargs):
        if kwargs:
            logger.bind(**kwargs).info(message)
        else:
            logger.bind(metadata_block=False).info(message)

    def log_debug(self, message):
        logger.debug(message)

    def log_critical(self, message):
        logger.critical(message)

    def _rotate_logs(self, message, file):
        file.seek(0, os.SEEK_END)
        if file.tell() > self.FILE_SYSTEM_LOGGER_FILE_SIZE:
            return True  # Rotate the log file
        return False  # Don't rotate the log file

    def context(self, **kwargs):
        return logger.contextualize(**kwargs)


MainLogger = FileSystemLoguruLogger()
