from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date, Boolean, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker, Session
from sqlalchemy.orm import declarative_base
from datetime import datetime
from models import *


class Controller:
    def __init__(self):
        self.session = Session(bind=engine)

    def login_chat(self, chat_id):
        chat = self.session.query(Chat).filter(Chat.id == chat_id).first()
        chat.is_login = True
        self.session.commit()

    def get_chat(self, chat_id):
        chats = self.session.query(Chat).where(Chat.id == chat_id).all()
        return chats

    def get_chats(self):
        chats = self.session.query(Chat).all()
        return chats

    def get_messages(self):
        messages = self.session.query(Chat).all()
        return messages

    def get_all_msgs_chat(self, chat_id):
        messages = self.session.query(Message).where(Message.chat_id == chat_id).all()
        return messages

    def get_not_menu_msgs_chat(self, chat_id):
        messages = self.session.query(Message).filter((Message.chat_id == chat_id) & (Message.is_menu == 0)).all()
        return messages

    def add_chat(self, chat_id, is_login=False):
        chat = Chat(id=chat_id, is_login=is_login)
        self.session.add(chat)
        self.session.commit()

    def add_message(self, message_id, text_message, chat_id, is_menu=False):
        message = Message(id=message_id, created_at=datetime.now(),
                          text_message=text_message, is_menu=is_menu, chat_id=chat_id)
        self.session.add(message)
        self.session.commit()

    def delete_all_msg_chat(self, chat_id):
        self.session.query(Message).where(Message.id == chat_id).delete()
        self.session.commit()

    def delete_message(self, message_id):
        self.session.query(Message).where(Message.id == message_id).delete()
        self.session.commit()

    def is_exist_menu_message(self, chat_id):
        messages = self.session.query(Message).where(Message.chat_id == chat_id).all()
        return len(messages) > 0


