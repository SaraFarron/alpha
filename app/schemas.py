from pydantic import BaseModel


class Index(BaseModel):
    id: int


class Employee(Index, BaseModel):
    name: str


class EmployeeCreate(BaseModel):
    name: str


class EmployeeDelete(Index, BaseModel):
    pass
