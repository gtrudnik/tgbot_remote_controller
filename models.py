from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date, Boolean, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker, Session
from sqlalchemy.orm import declarative_base

sqlite_database = "sqlite:///tgremotecontrollerbot.db"
engine = create_engine(sqlite_database)

Base = declarative_base()


class Chat(Base):
    __tablename__ = 'chats'
    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True
    )
    is_login = Column(Boolean)

    def __repr__(self):
        return f'{self.id} - {self.is_login}'


class Message(Base):
    __tablename__ = 'messages'
    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True
    )
    created_at = Column(DateTime)
    text_message = Column(Text)
    is_menu = Column(Boolean)
    chat_id = Column(Integer, ForeignKey('chats.id'))

    def __repr__(self):
        return f'{self.id} {self.created_at} {self.chat_id}'


Base.metadata.create_all(bind=engine)
