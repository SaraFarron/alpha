from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from auth import AuthHandler
import crud
import schemas

router = APIRouter()
auth_handler = AuthHandler()
users = []


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


@router.post('/register', status_code=201, tags=['auth'])
async def register(auth_details: schemas.AuthDetails):
    if any(x['username'] == auth_details.username for x in users):
        raise HTTPException(400, 'Username is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    users.append({
        'username': auth_details.username,
        'password': hashed_password
    })
    return


@router.post('/login', tags=['auth'])
async def login(auth_details: schemas.AuthDetails):
    user = None
    for x in users:
        if x['username'] == auth_details.username:
            user = x
            break

    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(401, 'Invalid username or password')
    token = auth_handler.encode_token(user['username'])
    return {'token': token}


@router.get('/unprotected', tags=['auth'])
async def unprotected():
    return {'hello': 'world'}


@router.get('/protected', tags=['auth'])
async def protected(username=Depends(auth_handler.auth_wrapper)):
    return {'name': username}
