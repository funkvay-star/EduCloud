from abc import ABC, abstractmethod, ABCMeta


class Logger:
    __metaclass__ = ABCMeta

    @abstractmethod
    def log_error(self, error):
        """Print error"""

    @abstractmethod
    def log_warning(self, message):
        """Print Warning"""

    @abstractmethod
    def log_info(self, message):
        """Print info"""
