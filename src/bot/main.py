import asyncio
import os

# aiogram modules
from aiogram import Bot, Dispatcher, types

# our exception handler
from src.Logger.exceptionHandler import handle_exceptions
from src.Logger.FileSystemLoguruLogger import MainLogger

# our modules
from src.bot.file_receiver import FileReceiver
from src.helperModules.definitions import TOKEN

STATUS_FILE_PATH = os.getenv("STATUS_FILE_PATH", "/tmp/bot_status.txt")


class TelegramBot:
    def __init__(self, token: str):
        self.bot = Bot(token)
        self.dp = Dispatcher()
        self.file_receiver = FileReceiver()
        MainLogger.log_info("Bot STARTED")

        # Create a status file
        with open(STATUS_FILE_PATH, "w") as f:
            f.write("Bot STARTED")

        # Register the content handler
        self.dp.message.register(self.content_handler)

    async def content_handler(self, message: types.Message) -> None:
        try:
            # Send the message to FileReceiver for classification and handling
            await self.file_receiver.classify_and_handle_message(message)

        except Exception as e:
            MainLogger.log_error(f"Error occurred: {e}")
            await message.answer("Error processing the message.")

    async def start_polling(self) -> None:
        await self.dp.start_polling(self.bot)


@handle_exceptions
async def main() -> None:
    bot = TelegramBot(TOKEN)
    await bot.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
