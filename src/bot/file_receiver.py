from aiogram import types
import json

# helper modules
from src.helperModules.definitions import MB

# our modules
from src.helperModules.message_helper import MessageHelper
from src.Logger.FileSystemLoguruLogger import MainLogger


class FileReceiver:
    DOCUMENT_SIZE_LIMIT = 100 * MB  # 100 MB
    VIDEO_SIZE_LIMIT = 500 * MB  # 500 MB

    async def classify_and_handle_message(self, message: types.Message):
        try:
            message_type = MessageHelper.determine_message_type(message)
            MainLogger.log_info(f"Message type determined: {message_type}")

            if message_type == "link":
                await self.handle_link(message)
            elif message_type == "document":
                await self.handle_document(message)
            elif message_type == "video":
                await self.handle_video(message)
            else:
                await self.handle_unknown_content(message)

        except Exception as e:
            MainLogger.log_error(f"Error occurred: {e}")
            await message.answer("Error processing the message.")

    async def handle_link(self, message: types.Message):
        MainLogger.log_info("Handling link")
        metadata = self.create_metadata(message)
        self.log_metadata(metadata)
        await message.answer("This is a link")

    async def handle_document(self, message: types.Message):
        MainLogger.log_info("Handling document")
        try:
            if message.document.file_size > self.DOCUMENT_SIZE_LIMIT:
                await message.answer("Document size exceeds 100 MB limit.")
                return
            metadata = self.create_metadata(message)
            self.log_metadata(metadata)
            await message.answer("Document received")
        except Exception as e:
            MainLogger.log_error(f"Error handling document: {e}")
            await message.answer("Error processing the document.")

    async def handle_video(self, message: types.Message):
        MainLogger.log_info("Handling video")
        try:
            if message.video.file_size > self.VIDEO_SIZE_LIMIT:
                await message.answer("Video size exceeds 500 MB limit.")
                return
            metadata = self.create_metadata(message)
            self.log_metadata(metadata)
            await message.answer("Video received")
        except Exception as e:
            MainLogger.log_error(f"Error handling video: {e}")
            await message.answer("Error processing the video.")

    async def handle_unknown_content(self, message: types.Message):
        MainLogger.log_info("Handling unknown content")
        await message.answer("Unknown content type")

    def create_metadata(self, message: types.Message):
        sender = message.from_user
        sender_id = sender.id if sender else None

        if sender and sender.username:
            sender_username = f"@{sender.username}"
        else:
            sender_username = "No username"

        sender_name = sender.first_name if sender else "No name"
        if sender and sender.last_name:
            sender_name += f" {sender.last_name}"

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

    def log_metadata(self, metadata):
        with MainLogger.context(metadata_block=True):
            metadata_log = {
                "event": "metadata_logging",
                "details": metadata
            }
            MainLogger.log_info(
                json.dumps(metadata_log, indent=2),
                metadata_block=True
                )

    def get_file_size(self, message: types.Message):
        message_type = MessageHelper.determine_message_type(message)

        if message_type == "document":
            return message.document.file_size
        elif message_type == "video":
            return message.video.file_size
        else:
            return 0  # No file size for other types (like link or text)
