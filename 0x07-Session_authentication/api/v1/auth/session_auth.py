#!/usr/bin/env python3
""" 1.Empty session
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    class sessionauth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        create_session
        """
        if user_id is None or type(user_id) is not str:
            return None
        id_session = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[id_session] = user_id
        return id_session

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_id_for_session
        """
        if session_id is None or type(session_id) is not str:
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)
