from sqlalchemy import Column, Integer, String
from database import Base


class Index:
    id = Column(Integer, primary_key=True, index=True)


class Employee(Base, Index):
    __tablename__ = 'employees'

    name = Column(String)
