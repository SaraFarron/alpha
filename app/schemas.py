from pydantic import BaseModel, Field, EmailStr
from datetime import time


class TaskBase(BaseModel):
    title: str
    description: str | None = None
    time_to_complete: time
    price: float

    class Config:
        arbitrary_types_allowed = True


class TaskCreate(TaskBase):
    title: str
    description: str | None
    price: float
    time_to_complete: time

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "task title",
                "description": "task description",
                "price": 100,
                "time_to_complete": "01:00:00",
            }
        }


class TaskUpdate(BaseModel):
    title: str | None
    description: str | None
    price: float | None
    user_id: int | None
    is_completed: bool | None
    time_to_complete: time | None

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "task title",
                "description": "task description",
                "price": 150,
                "user_id": 1,
                "is_completed": True,
                "time_to_complete": "01:30:00",
            }
        }


class Task(TaskBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    fullname: str
    email: str
    access_level: int
    task_load: int
    success_ratio: float | None
    score: int

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    email: str | None
    fullname: str | None
    access_level: int | None
    task_load: int | None
    success_ratio: float | None
    score: int | None

    class Config:
        schema_extra = {
            "example": {
                "email": "john@x.com",
                "fullname": "John Doe",
                "access_level": 1,
                "task_load": 0,
                "success_ratio": 50.1,
                "score": 80,
            }
        }


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    access_level: int | None
    task_load: int | None

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "john@x.com",
                "password": "weakpassword",
                "access_level": 1,
                "task_load": 0,
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


class AccessToken(BaseModel):
    access_token: str
