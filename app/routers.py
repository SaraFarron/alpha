from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import crud
import schemas

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/')
async def api_overview(): return {'success': 'indeed'}


@router.get('/employees', tags=['employees'])
async def read_employees(db: Session = Depends(get_db)):
    employees = crud.get_employees(db)
    return employees


@router.get('/employee/{employee_id}', tags=['employees'])
async def read_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)
    if employee:
        return employee
    else:
        raise HTTPException(404)


@router.post('/employees', tags=['employees'], response_model=schemas.Employee)
async def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, 100)
    if db_employee:
        raise HTTPException(400, detail='Employee already exists')
    response = crud.new_employee(db, employee)
    print('\n', response)
    return {'status': 200}
