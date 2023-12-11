import re
from aiogram import types
import sys
from pathlib import Path

# to include other modules
src_path = Path(__file__).resolve().parents[1]
sys.path.append(str(src_path))

# our modules
from helperModules.string_helper import StringHelper


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
