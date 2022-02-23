from pydantic import BaseModel


class Employee(BaseModel):
    id: int
    name: str


class EmployeeCreate(BaseModel):
    name: str


class TaskBase(BaseModel):
    title: str
    description: str | None = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    employee_id: int
    title: str
    description: str | None = None


class Task(TaskBase):
    id: int
    employee_id: int

    class Config:
        orm_mode = True
