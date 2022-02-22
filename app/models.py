from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Index:
    id = Column(Integer, primary_key=True, index=True)


class Employee(Base, Index):
    __tablename__ = 'employees'

    name = Column(String)


class Task(Base, Index):
    __tablename__ = 'tasks'

    title = Column(String, index=True)
    description = Column(String, index=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
