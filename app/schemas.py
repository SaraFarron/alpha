from pydantic import BaseModel
from sqlalchemy import Time


class Employee(BaseModel):
    id: int
    name: str


class EmployeeCreate(BaseModel):
    name: str


class TaskBase(BaseModel):
    title: str
    description: str | None = None
    time_to_complete: Time

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
