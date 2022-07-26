from sqlalchemy import (
    Column, Integer, String, ForeignKey,
    Date, Time, DateTime, Boolean, Float
)
from datetime import datetime
from database import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    is_completed = Column(Boolean, default=False, nullable=False)
    time_to_complete = Column(Time, nullable=False)
    datetime_received = Column(DateTime, default=datetime.utcnow)
    datetime_completed = Column(DateTime)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, nullable=False)
    date_employed = Column(Date, nullable=False, default=datetime.utcnow().date)
    access_level = Column(Integer, default=1, nullable=False)
    task_load = Column(Integer, default=0)
    success_ratio = Column(Float)
    score = Column(Integer, default=100)

