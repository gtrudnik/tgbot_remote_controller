from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date, Boolean, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker, Session
from sqlalchemy.orm import declarative_base

sqlite_database = "sqlite:///tgremotecontrollerbot.db"
engine = create_engine(sqlite_database)

Base = declarative_base()


class Chat(Base):
    __tablename__ = 'chats'
    chat_id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True
    )
    is_login = Column(Boolean)

    def __repr__(self):
        return f'{self.chat_id} - {self.is_login}'


class Message(Base):
    __tablename__ = 'messages'
    message_id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True
    )
    created_at = Column(DateTime)
    text_message = Column(Text)
    chat_id = Column(Integer, ForeignKey('chats.chat_id'))

    def __repr__(self):
        return f'{self.message_id} {self.created_at} {self.chat_id}'


Base.metadata.create_all(bind=engine)
