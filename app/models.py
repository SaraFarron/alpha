from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime, Date, Table
from database import Base
from sqlalchemy.orm import relationship


class BaseIndex(Base):
    id = Column(Integer, primary_key=True, index=True)


class BaseName(Base):
    name = Column(String)


class Product(BaseIndex, BaseName):
    __tablename__ = 'products'

    current_volume = Column(Float)


class Batch(BaseIndex):
    __tablename__ = 'batches'

    product = Column(Integer, ForeignKey('products.id'))
    number = Column(Integer)
    date_time = Column(DateTime)
    weight = Column(Float)
    supplier = Column(String)
    quantity = Column(Float)
    tank = Column(Integer, ForeignKey('tanks.id'))
    density = Column(Float)  # read-only
    received_shift = Column(String)


class Tank(BaseIndex, BaseName):
    __tablename__ = 'tanks'

    capacity = Column(Float)


class Supplier(BaseIndex, BaseName):
    __tablename__ = 'suppliers'


class Employee(BaseIndex):
    __tablename__ = 'employees'

    full_name = Column(String)
    date_of_employment = Column(Date)
    date_of_layoff = Column(Date)
    sex = Column(String)  # Make choices?
    experience = Column(Integer)  # read-only
    date_of_birth = Column(Date)


class Trade(BaseIndex):
    __tablename__ = 'trades'

    total = Column(Float)
    date_time = Column(DateTime)
    shift = Column(Integer, ForeignKey('shifts.id'))


shift_employee = Table('shift_employee', Base.metadata,
                       Column('shift_id', ForeignKey('shifts.id'), primary_key=True),
                       Column('employee_id', ForeignKey('employees.id'), primary_key=True)
                       )


class Shift(BaseIndex):
    __tablename__ = 'shifts'

    employees = relationship('Employee', secondary='shift_employee', back_populates='shifts')
