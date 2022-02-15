from pydantic import BaseModel


class Product(BaseModel):
    name: str
    current_volume: float

    class Config:
        orm_mode = True


# class Batch(BaseModel):
#     product: fk
#     number: int
#     date_time: datetime
#     weight: float
#     supplier: str
#     quantity: float
#     tank: fk
#     density: float(read_only=True)
#     received_shift: str
