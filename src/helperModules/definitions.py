import os
from dotenv import dotenv_values

config = dotenv_values('.env')
TOKEN = config.get('TOKEN')
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
MB = 1024 * 1024
