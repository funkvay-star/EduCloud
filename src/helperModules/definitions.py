from dotenv import dotenv_values

config = dotenv_values('.env')

TOKEN = config.get('TOKEN')
