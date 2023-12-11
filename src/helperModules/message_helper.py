from aiogram import types

# our modules
from src.helperModules.string_helper import StringHelper


class MessageHelper:

    @staticmethod
    def determine_message_type(message: types.Message):
        message_content = message.text or ""
        if StringHelper.is_url(message_content):
            return "link"
        elif isinstance(message.document, types.Document):
            return "document"
        elif isinstance(message.video, types.Video):
            return "video"
        else:
            return "unknown"
