#!/usr/bin/env python3
"""
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """
    """

    def require_auth(self, path: str, excluded_path: List[str]) -> bool:
        """
        """
        if path is None or excluded_path is None:
            return True
        return False 

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