from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date, Boolean, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker, Session
from sqlalchemy.orm import declarative_base
from datetime import datetime
from models import *


class Controller:
    def __init__(self):
        self.session = Session(bind=engine)

    def get_chats(self):
        chats = self.session.query(Chat).all()
        return chats

    def get_messages(self):
        messages = self.session.query(Chat).all()
        return messages

    def add_chat(self, chat_id, is_login=False):
        chat = Chat(chat_id=chat_id, is_login=is_login)
        self.session.add(chat)
        self.session.commit()

    def add_message(self, message_id, text_message, chat_id):
        message = Message(message_id=message_id, created_at=datetime.now(),
                          text_message=text_message, chat_id=chat_id)
        self.session.add(message)
        self.session.commit()
