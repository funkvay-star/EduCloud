from functools import wraps
from src.Logger.FileSystemLoguruLogger import MainLogger

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            MainLogger.log_error(f"Exception in {func.__name__}: {e}")
            raise
    return wrapper
