#!usr/bin/env python3
"""
filtered logger module
"""

import re


def filter_datum(fields, redaction, message, separator) -> str:
    '''obfuscates log messages'''
    r = ''
    for msg in message.split(";"):
        param = msg.split("=")
        if param[0] in fields:
            param[1] = re.sub(str(param[1]), redaction, param[1])
            r += param[0] + "=" + param[1] + separator
            continue
        r = r + msg + separator
    return r
