
from src.Logger.FileSystemLoguruLogger import MainLogger


def handle_exceptions(func):
    def result():
        try:
            func()
        except Exception as e:
            MainLogger.log_error(e)

    return result
