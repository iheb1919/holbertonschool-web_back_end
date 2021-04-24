#!/usr/bin/env python3
"""
3. Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """
    3. Auth class
    """

    def require_auth(self, path: str, excluded_path: List[str]) -> bool:
        """
        require function
        """
        if path is None or excluded_path is None or excluded_path == '':
            return True
        if path[len(path) - 1] != '/':
            path += '/'
        for item in excluded_path:
            if path == item:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization_header function
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current_user function
        """
        return None
