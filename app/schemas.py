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

    class Config:
        arbitrary_types_allowed = True


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    employee_id: int
    title: str
    description: str | None = None
    is_completed: bool = False


class Task(TaskBase):
    id: int
    employee_id: int

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
