from pydantic import BaseModel, Field
from datetime import datetime, date


class BaseIndex(BaseModel):
    id: int = Field(primary_key=True, index=True)


class BaseName(BaseModel):
    name: str


class Product(BaseName, BaseIndex):
    current_volume: float

    class Config:
        orm_mode = True


class Batch(BaseIndex):
    product: int
    number: int
    date_time: datetime
    weight: float
    supplier: str
    quantity: float
    tank: int
    density: float
    received_shift: str


class Tank(BaseIndex, BaseName):
    capacity: float


class Supplier(BaseIndex, BaseName):
    pass


class Employee(BaseIndex):
    full_name: str
    date_of_employment: date
    date_of_layoff: date
    sex: str  # Make choices?
    experience: int  # read-only
    date_of_birth: date


class Trade(BaseIndex):
    total: float
    date_time: datetime
    shift: int


class Shift(BaseIndex):
    employees: list[int, ]
