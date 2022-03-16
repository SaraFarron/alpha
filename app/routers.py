from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import time
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


@router.post('/employees', tags=['employees'], response_model=schemas.Employee, status_code=201)
async def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)) -> schemas.Employee:
    db_employee = crud.get_employee_by_name(db, employee.name)
    if db_employee:
        raise HTTPException(400, detail='Employee already exists')
    response = crud.new_employee(db, employee)

    # pydantic requires response to be a dictionary
    return response.__dict__


@router.delete('/employee/{employee_id}', tags=['employees'], status_code=204)
async def destroy_employee(employee_id: int, db: Session = Depends(get_db)):
    return crud.delete_employee(db, employee_id)


@router.post("/employees/{employee_id}/task/", response_model=schemas.Task, tags=['tasks'], status_code=201,
             description='time format: H:M:S')
async def create_task_for_employee(
    employee_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)
):
    return crud.create_employee_task(db=db, task=task, employee_id=employee_id)


@router.get("/tasks/", response_model=list[schemas.Task], tags=['tasks'])
async def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks


@router.get('/task/{task_id}', response_model=schemas.Task, tags=['tasks'])
async def read_task(task_id: int, db: Session = Depends(get_db)):
    return crud.get_task(db, task_id)


@router.patch('/task/{task_id}', response_model=schemas.TaskUpdate, tags=['tasks'])
async def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    return crud.update_task(task_id, db, task)


@router.delete('/tasks/{task_id}', tags=['tasks'], status_code=204)
async def destroy_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(task_id, db)
