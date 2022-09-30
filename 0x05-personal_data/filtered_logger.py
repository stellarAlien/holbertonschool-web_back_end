#!usr/bin/env python3
"""
filtered logger module
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    '''obfuscates log messages'''
    for field in fields:
        message = re.sub(f"{field}=(.*?;)",f"{field}={redaction}{separator}", message)
    return message