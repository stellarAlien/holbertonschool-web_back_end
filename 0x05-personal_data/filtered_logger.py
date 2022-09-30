#!usr/bin/env python3
"""
filtered logger module
"""

import re


def filter_datum(fields, redaction, message, separator) -> str:
    '''obfuscates log messages'''
    for field in fields:
        message = re.sub(f"{field}=(.*?;)",f"{field}={redaction}{separator}", message)
    return message