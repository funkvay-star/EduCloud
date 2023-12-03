import asyncio
from dotenv import dotenv_values
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


config = dotenv_values('.env')

API_TOKEN = config.get('TOKEN')
print(API_TOKEN)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я бот, который отвечает на приветствия!")

@dp.message(lambda message: message.text.lower() == 'привет')
async def say_hi(message: types.Message):
    await message.answer("Привет! Как дела?")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
