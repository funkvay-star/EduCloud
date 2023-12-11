import re
import logging
from aiogram import types
import sys
from pathlib import Path

# to include other modules
src_path = Path(__file__).resolve().parents[1]
sys.path.append(str(src_path))

# our modules
from helperModules.message_helper import MessageHelper


class FileReceiver:
    MB = 1024 * 1024  # Bytes in megabyte
    DOCUMENT_SIZE_LIMIT = 100 * MB  # 100 MB
    VIDEO_SIZE_LIMIT = 500 * MB  # 500 MB

    async def classify_and_handle_message(self, message: types.Message):
        try:
            message_type = MessageHelper.determine_message_type(message)

            if message_type == "link":
                await self.handle_link(message)
            elif message_type == "document":
                await self.handle_document(message)
            elif message_type == "video":
                await self.handle_video(message)
            else:
                await self.handle_unknown_content(message)

        except Exception as e:
            logging.error(f"Error occurred: {e}")
            await message.answer("Error processing the message.")

    async def handle_link(self, message: types.Message):
        # TODO Handle link-specific logic
        metadata = self.create_metadata(message)
        self.print_metadata(metadata)
        await message.answer("This is a link")

    async def handle_document(self, message: types.Message):
        # TODO Handle document-specific logic, including size check
        if message.document.file_size > self.DOCUMENT_SIZE_LIMIT:
            await message.answer("Document size exceeds 100 MB limit.")
            return
        metadata = self.create_metadata(message)
        self.print_metadata(metadata)
        # TODO Further processing (e.g., storage)

    async def handle_video(self, message: types.Message):
        # TODO Handle video-specific logic, including size check
        if message.video.file_size > self.VIDEO_SIZE_LIMIT:
            await message.answer("Video size exceeds 500 MB limit.")
            return
        metadata = self.create_metadata(message)
        self.print_metadata(metadata)
        # TODO Further processing (e.g., storage)

    async def handle_unknown_content(self, message: types.Message):
        # TODO Handle unknown content type logic
        await message.answer("Unknown content type")

    def create_metadata(self, message: types.Message):
        sender = message.from_user
        sender_id = sender.id if sender else None

        if sender and sender.username:
            sender_username = f"@{sender.username}"
        else:
            sender_username = "No username"

        if sender:
            sender_name = sender.first_name
            if sender.last_name:
                sender_name += f" {sender.last_name}"
        else:
            sender_name = "No name"

        message_type = MessageHelper.determine_message_type(message)
        iso_formatted_date = message.date.isoformat()
        file_size = self.get_file_size(message)

        metadata = {
            "sender_id": sender_id,
            "sender_username": sender_username,
            "sender_name": sender_name,
            "message_type": message_type,
            "iso_formatted_date": iso_formatted_date,
            "file_size in bytes": file_size,
        }

        return metadata

    def print_metadata(self, metadata):
        for key, value in metadata.items():
            print(f"{key}: {value}")

    def get_file_size(self, message: types.Message):
        message_type = MessageHelper.determine_message_type(message)

        if message_type == "document":
            return message.document.file_size
        elif message_type == "video":
            return message.video.file_size
        else:
            # No file size for other types (like link or text)
            return 0
