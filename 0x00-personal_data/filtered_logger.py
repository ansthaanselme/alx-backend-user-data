#!/usr/bin/env python3
"""
filtered_logger file
"""
import re


def filter_datum(fields, redaction, message, separator):
    req = message
    for loop in message.split(';'):
        ch= loop.split('=')
        if ch[0] in fields:
            req = re.sub(ch[1], redaction, req)
    return req