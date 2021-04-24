#!/usr/bin/env python3
"""
6. Basic auth
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User

class BasicAuth(Auth):
    """
    basicauth class
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None or type(authorization_header) is not str:
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]
    
        