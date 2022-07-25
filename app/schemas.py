from pydantic import BaseModel, Field, EmailStr
from datetime import time


class Employee(BaseModel):
    id: int
    name: str


class EmployeeCreate(BaseModel):
    name: str


class TaskBase(BaseModel):
    title: str
    description: str | None = None
    time_to_complete: time
    price: float

    class Config:
        arbitrary_types_allowed = True


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    user_id: int | None = None
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None
    price: float | None = None


class Task(TaskBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "john@x.com",
                "password": "weakpassword"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "john@x.com",
                "password": "weakpassword"
            }
        }
