from fastapi import APIRouter, Depends

from database import get_db
from auth import JWTBearer
from crud import *
import schemas

router = APIRouter(
    prefix='/tasks',
    tags=['tasks'],
    dependencies=[Depends(JWTBearer())]
)


@router.get('/', response_model=list[schemas.Task])
async def read_tasks(db: Session = Depends(get_db)): return get_tasks(db)


@router.get('/{task_id}/', response_model=schemas.Task)
async def read_task(task_id: int, db: Session = Depends(get_db)): return get_task(db, task_id)


@router.post('/new/', response_model=schemas.Task, status_code=201, description='time format: HH:MM:SS')
async def new_task(
        employee_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)
): return create_employee_task(db=db, task=task, employee_id=employee_id)


@router.put('/update/{task_id}/', response_model=schemas.TaskUpdate)
async def edit_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    return update_task(task_id, db, task)


@router.delete('/remove/{task_id}/', status_code=204)
async def remove_task(task_id: int, db: Session = Depends(get_db)): return delete_task(task_id, db)
