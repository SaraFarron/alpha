from pydantic import BaseModel, Field, EmailStr
from datetime import time, datetime, date


class TaskBase(BaseModel):
    title: str
    description: str | None
    price: float
    time_to_complete: time

    class Config:
        arbitrary_types_allowed = True


class TaskCreate(TaskBase):

    class Config:
        schema_extra = {
            "example": {
                "title": "task title",
                "description": "task description",
                "price": 100,
                "time_to_complete": "01:00:00",
            }
        }


class TaskUpdate(TaskBase):
    title: str | None
    price: float | None
    user_id: int | None
    is_completed: bool | None
    time_to_complete: time | None

    class Config:
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
    is_completed: bool
    datetime_received: datetime
    datetime_completed: datetime | None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "task title",
                "description": "task description",
                "price": 150,
                "user_id": 1,
                "is_completed": True,
                "time_to_complete": "01:30:00",
                "datetime_received": "2022-07-25 13:52:29.392925",
                "datetime_completed": "2022-07-26 16:21:45.230490",
            }
        }


class UserBase(BaseModel):
    fullname: str
    email: str
    date_employed: date

    class Config:
        arbitrary_types_allowed = True


class UserResponse(UserBase):
    id: int
    access_level: int
    task_load: int
    success_ratio: float | None
    score: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "fullname": "username",
                "email": "example@test.com",
                "date_employed": "2022-07-25 13:52:29.392925",
                "access_level": 1,
                "task_load": 10,
                "success_ration": 50.1,
                "score": 100,
            }
        }


class UserUpdate(BaseModel):
    fullname: str | None
    email: str | None
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
