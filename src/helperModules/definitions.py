import os
from dotenv import dotenv_values

config = dotenv_values('.env')
TOKEN = config.get('TOKEN')
LOG_DIR = config.get('LOG_DIR')
ROOT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'bot')
MB = 1024 * 1024 # Define MB as 1,048,576 bytes
