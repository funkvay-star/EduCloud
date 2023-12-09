import re
import logging
from aiogram import types

class FileReceiver:
    async def classify_and_handle_message(self, message: types.Message):
        try:
            message_content = message.text or ""
            if re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message_content):
                await message.answer("This is a link")
            elif isinstance(message.document, types.Document):
                await message.answer("This is a document")
            elif isinstance(message.video, types.Video):
                await message.answer("This is a video")
            else:
                await message.answer("Unknown content type")
                
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            await message.answer("An error occurred while processing the message.")
