from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from auth import JWTBearer
from crud import (
    get_all, get_concrete, update_entry,
    create_entry, delete_entry,
)
import schemas
import models

router = APIRouter(
    prefix='/tasks',
    tags=['tasks'],
    dependencies=[Depends(JWTBearer())]
)


@router.get('/', response_model=list[schemas.Task])
async def read_tasks(db: Session = Depends(get_db)):
    return get_all(db, models.Task)


@router.get('/{task_id}/', response_model=schemas.Task)
async def read_task(task_id: int, db: Session = Depends(get_db)):
    return get_concrete(db, models.Task, {'id': task_id})


@router.post(
    '/',
    response_model=schemas.Task,
    status_code=201,
    description='time format: HH:MM:SS'
)
async def new_task(user_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    task = task.dict() | {'user_id': user_id}
    return create_entry(db, models.Task, task)


@router.patch('/update/{task_id}/', response_model=schemas.TaskUpdate)
async def edit_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    return update_entry(db, models.Task, task_id, task.dict()).__dict__  # pydantic wants dictionary


@router.delete('/remove/{task_id}/', status_code=204)
async def remove_task(task_id: int, db: Session = Depends(get_db)):
    return delete_entry(db, models.Task, task_id)
