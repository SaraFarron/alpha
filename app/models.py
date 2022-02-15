from sqlalchemy import Column, String, Float, Integer
from database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    current_volume = Column(Float)
