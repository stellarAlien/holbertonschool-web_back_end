#!usr/bin/env python3
"""
filtered logger module
"""
import logging
import re
from typing import List



class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields
        
    def format(self, record: logging.LogRecord) -> str:
        record.msg = self.filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)

    def filter_datum(self, fields: List[str], redaction: str, message: str, separator: str) -> str:
        '''obfuscates log messages'''
        for field in fields:
            message = re.sub(f"{field}=(.*?;)",f"{field}={redaction}{separator}", message)
        return message