#!/usr/bin/env python3

'''
session auth module
'''

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    '''session auth mechanism'''

    def __init__(self) -> None:
        '''instantiate an instance'''
        super().__init__()
        self.user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        '''create a session id for a user id'''
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''return user of session'''
        if not session_id or type(session_id) is not str:
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id
