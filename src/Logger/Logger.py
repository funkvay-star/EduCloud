from abc import ABC, abstractmethod, ABCMeta

class Logger(metaclass=ABCMeta):
    @abstractmethod
    def log_error(self, error):
        """Log an error"""

    @abstractmethod
    def log_warning(self, message):
        """Log a warning"""

    @abstractmethod
    def log_info(self, message):
        """Log an info"""

    @abstractmethod
    def log_debug(self, message):
        """Log a debug message"""

    @abstractmethod
    def log_critical(self, message):
        """Log a critical message"""
