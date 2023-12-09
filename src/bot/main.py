import re
import asyncio
import logging
import sys
from os import getenv
from typing import Any
from dotenv import dotenv_values

from aiogram import Bot, Dispatcher, types
from aiogram.types import Document, Video

config = dotenv_values('.env')
TOKEN = config.get('TOKEN')


class TelegramBot:
    def __init__(self, token: str):
        self.bot = Bot(token)
        self.dp = Dispatcher()

        # Register the content handler
        self.dp.message.register(self.content_handler)

    async def content_handler(self, message: types.Message) -> None:
        try:
            message_content = message.text or ""
            if re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message_content):
                await message.answer("This is a link")
            elif isinstance(message.document, Document):
                await message.answer("This is a document")
            elif isinstance(message.video, Video):
                await message.answer("This is a video")
            else:
                await message.answer("Unknown content type")

        except Exception as e:
            logging.error(f"Error occurred: {e}")
            await message.answer("An error occurred while processing the message.")

    async def start_polling(self) -> None:
        await self.dp.start_polling(self.bot)

async def main() -> None:
    bot = TelegramBot(TOKEN)
    await bot.start_polling()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
