from Logger.Logger import Logger
from loguru import logger
import os

from src.helperModules.definitions import ROOT_DIR, MB


class FileSystemLoguruLogger(Logger):
    FILE_SYSTEM_LOGGER_FILE_SIZE = 500 * MB

    def __init__(self):
        self._log_path = ROOT_DIR + "/application.log"
        logger.add(self._log_path, format="{time} {level} {message}", backtrace=True, )

    def log_error(self, error: Exception):
        logger.error(error)

    def log_warning(self, message):
        logger.warning(message)

    def log_info(self, message):
        logger.info(message)

    def _rotate_logs(self):
        file_size = os.stat(self._log_path)
        if file_size > self.FILE_SYSTEM_LOGGER_FILE_SIZE:
            self._clear_logs()
    def _clear_logs(self):
        os.remove(self._log_path)


MainLogger = FileSystemLoguruLogger()
