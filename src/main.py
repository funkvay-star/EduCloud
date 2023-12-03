import os

from Logger.exceptionHandler import init_exception_handling

# Get the environment variable
token = os.getenv('TELEGRAM_TOKEN')

init_exception_handling()
# Check if the token is available
if token:
    raise Exception("test", 'testabcd')
    print("Token:", token)
else:
    print("TELEGRAM_TOKEN not found")

