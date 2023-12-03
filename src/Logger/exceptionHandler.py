import sys
import time

from Logger.FileSystemLoguruLogger import MainLogger



def init_exception_handling():
    def exception_hook(type, value, traceback):
        if type == KeyboardInterrupt:
            pass
        else:
            print("exception handled")
            MainLogger.log_error(value)
            sys.__excepthook__(type, value, traceback)

    sys.excepthook = exception_hook
