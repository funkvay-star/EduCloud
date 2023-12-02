import os

# Get the environment variable
token = os.getenv('TELEGRAM_TOKEN')

# Check if the token is available
if token:
    print("Token:", token)
else:
    print("TELEGRAM_TOKEN not found")

