from Logger.Logger import Logger
from definitions import ROOT_DIR
from loguru import logger


class FileSystemLoguruLogger(Logger):

    def __init__(self):
        self._log_path = ROOT_DIR + "/application.log"
        logger.add(self._log_path, rotation="500 MB", format="{time} {level} {message}", backtrace=True, )

    def log_error(self, error: Exception):
        print('exception logged')
        logger.error(error)

    def log_warning(self, message):
        logger.warning(message)

    def log_info(self, message):
        logger.info(message)


MainLogger = FileSystemLoguruLogger()
