import re


class StringHelper:
    URL_PATTERN = (
        r'http[s]?://'  # Scheme
        r'(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]'
        r'|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    )

    @staticmethod
    def is_url(message_content):
        return re.match(StringHelper.URL_PATTERN,
                        message_content)
