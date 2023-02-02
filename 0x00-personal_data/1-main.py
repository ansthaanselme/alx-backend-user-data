#!/usr/bin/env python3
"""
Main file
"""

import logging
import re

RedactingFormatter = __import__('filtered_logger').RedactingFormatter

message = "name=bob;email=bob@test.com;ssn=000-123-0000;password=P@ssw0rd;"
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))
