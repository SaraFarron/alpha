from sqlalchemy.orm import Session

import models
import schemas


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employees(db: Session):
    return db.query(models.Employee).all()


def new_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(name=employee.name)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee
