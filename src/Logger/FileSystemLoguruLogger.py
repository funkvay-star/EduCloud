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
        logger.remove()
        logger.add(sys.stderr, level="DEBUG")
        logger.add(self._log_path, 
                   format="{time} {level} {message}", 
                   backtrace=True,
                   rotation=self._rotate_logs,
                   retention="10 days")  # Keep log files for 10 days
        logger.info(f"Logger initialized. Log path: {self._log_path}")

    def log_error(self, error: Exception):
        logger.error(error)

    def log_warning(self, message):
        logger.warning(message)

    def log_info(self, message):
        logger.info(message)

    def log_debug(self, message):
        logger.debug(message)

    def log_critical(self, message):
        logger.critical(message)

    def _rotate_logs(self, message, file):
        file.seek(0, os.SEEK_END)
        if file.tell() > self.FILE_SYSTEM_LOGGER_FILE_SIZE:
            return True  # Rotate the log file
        return False  # Don't rotate the log file

MainLogger = FileSystemLoguruLogger()
