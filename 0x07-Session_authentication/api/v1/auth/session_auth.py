#!/usr/bin/env python3

from api.v1.auth.auth import Auth
import uuid

class SessionAuth(Auth):
    '''session auth mechanism'''
    
    def __init__(self) -> None:
        super().__init__()
        self.user_id_by_session_id = {}
    
    def create_session(self, user_id: str = None) -> str:
        '''create a session id for a user id'''
        if user_id is None:
            return None
        if type(user_id) != str:
            return None
        session_id = uuid.uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
