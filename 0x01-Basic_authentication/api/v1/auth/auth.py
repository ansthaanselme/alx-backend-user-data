#!/usr/bin/env python3
"""Authentication Module"""

from flask import request
from typing import List, TypeVar


class Auth:
    """class Auth, that manages API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method to validate if endpoint requires auth."""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        path_l = len(path)
        slash_path = True if path[path_l - 1] == '/' else False

        tmp_path = path
        if not slash_path:
            tmp_path += '/'
        for exec in excluded_paths:
            exec_l = len(exec)
            if exec_l == 0:
                continue
            if exec[exec_l - 1] != '*':
                if tmp_path == exec:
                    return False
            else:
                if exec[:-1] == path[:exec_l - 1]:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """handles auth header"""
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """validates current user"""
        return None
