import asyncio
import logging
import sys
from dotenv import dotenv_values
from pathlib import Path

# aiogram modules
from aiogram import Bot, Dispatcher, types

# our modules
from src.bot.file_receiver import FileReceiver
from src.helperModules.definitions import TOKEN


class TelegramBot:
    def __init__(self, token: str):
        self.bot = Bot(token)
        self.dp = Dispatcher()
        self.file_receiver = FileReceiver()

        # Register the content handler
        self.dp.message.register(self.content_handler)

    async def content_handler(self, message: types.Message) -> None:
        try:
            # Send the message to FileReceiver for classification and handling
            await self.file_receiver.classify_and_handle_message(message)

        except Exception as e:
            logging.error(f"Error occurred: {e}")
            await message.answer("Error processing the message.")

    async def start_polling(self) -> None:
        await self.dp.start_polling(self.bot)


async def main() -> None:
    bot = TelegramBot(TOKEN)
    await bot.start_polling()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
