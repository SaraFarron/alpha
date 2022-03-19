from sqlalchemy.orm import Session
from fastapi import HTTPException

import models
import schemas
from auth import Hasher


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employee_by_name(db: Session, employee_name: str):
    return db.query(models.Employee).filter(models.Employee.name == employee_name).first()


def get_employees(db: Session):
    return db.query(models.Employee).all()


def new_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(name=employee.name)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.Employee).get(employee_id)
    if db_employee:
        db.delete(db_employee)
        db.commit()
    else:
        raise HTTPException(404, detail=f'employee with id {employee_id} not found')
    return


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def get_task(db: Session, id: int):
    task = db.query(models.Task).get(id)
    if task:
        return task
    else:
        raise HTTPException(404, f'task with id {id} not found')


def create_employee_task(db: Session, task: schemas.TaskCreate, employee_id: int):
    db_task = models.Task(**task.dict(), employee_id=employee_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(id: int, db: Session, task: schemas.TaskUpdate):
    db_task = get_task(db, id)
    task_data = task.dict(exclude_unset=True)
    for k, v in task_data.items():
        setattr(db_task, k, v)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return task


def delete_task(id: int, db: Session):
    task = get_task(db, id)
    db.delete(task)
    db.commit()
    return task


def get_users(db: Session): return db.query(models.User).all()


def new_user(db: Session, user: schemas.UserSchema):
    hashed_password = Hasher.get_password_hash(user.password)
    db_user = models.User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
