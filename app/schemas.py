from pydantic import BaseModel


class Index:
    id: int


class Employee(Index, BaseModel):
    name: str


class EmployeeCreate(Employee):
    pass
