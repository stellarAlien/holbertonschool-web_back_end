#!/usr/bin/env python3

from datetime import datetime
from api.v1.auth.session_auth import SessionAuth
import os

class SessionExpAuth(SessionAuth):
    '''session with expiration'''

    def __init__(self):
        '''init method'''
        super.__init__
        try:
            duration = int(os.getenv("SESSION_DURATION", 0))
        except Exception:
            duration = 0
        self.user_id_by_session_id = dict()
        self.session_duration = duration
    
    def create_session(self, user_id=None):
        '''create session'''
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        self.user_id_by_session_id["session dictionary"] = session_id
        self.user_id_by_session_id["user_id"] = user_id
        self.user_id_by_session_id["created_at"] = datetime.now()
        return session_id
    
    def user_id_for_session_id(self, session_id=None):
        '''user id for session'''
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id.keys():
            return None
        if self.session_duration == 0:
            return self.user_id_by_session_id["user_id"]
        if self.user_id_by_session_id.get('created_at') is None:
            return None
        created_at = self.user_id_by_session_id.get('created_at')
        delta = datetime.timedelta(self.session_duration + created_at)
        if delta < datetime.now():
            return None
        
        return self.user_id_by_session_id.get("user_id")