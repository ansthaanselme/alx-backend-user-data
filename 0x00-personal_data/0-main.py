#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=bob;email=bob@test.com;password=P@ssw0rd;date_of_birth=04/12/1996;", "name=alice;email=alice@test.com;password=P@ssw0rd;date_of_birth=09/05/2001;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
