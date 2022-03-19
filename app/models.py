from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, DateTime, Boolean
from database import Base


class Index:
    id = Column(Integer, primary_key=True, index=True)


class Employee(Base, Index):
    __tablename__ = 'employees'

    name = Column(String, index=True)
    date_employed = Column(Date)
    task_load = Column(Integer, default=0)


class Task(Base, Index):
    __tablename__ = 'tasks'

    title = Column(String, index=True)
    description = Column(String, index=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    is_completed = Column(Boolean, default=False, index=True)
    time_to_complete = Column(Time)
    datetime_received = Column(DateTime)


class User(Base, Index):
    __tablename__ = 'users'

    fullname = Column(String, index=True, unique=True)
    email = Column(String, index=True, unique=True)
    password = Column(String)
    access_level = Column(Integer, index=True, default=1)
