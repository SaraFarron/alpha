from pydantic import BaseModel


class Index(BaseModel):
    id: int


class Employee(Index, BaseModel):
    name: str


class EmployeeCreate(BaseModel):
    name: str


class EmployeeDelete(Index, BaseModel):
    pass


class TaskBase(BaseModel):
    title: str
    description: str | None = None


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    employee_id: int

    class Config:
        orm_mode = True
