from fastapi import APIRouter, Depends

from database import get_db
from auth import JWTBearer
from crud import *
import schemas

router = APIRouter(
    prefix='/management',
    tags=['management'],
    dependencies=[Depends(JWTBearer())]
)


@router.get('/')
async def read_employees(db: Session = Depends(get_db)): return get_employees(db)


@router.get('/{employee_id}/')
async def read_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = get_employee(db, employee_id)
    if employee:
        return employee
    else:
        raise HTTPException(404, 'User does not exist')


@router.post('/new/', response_model=schemas.Employee, status_code=201)
async def new_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = get_employee_by_name(db, employee.name)
    if db_employee:
        raise HTTPException(400, detail='Employee already exists')
    response = new_employee(db, employee)

    # pydantic requires response to be a dictionary
    return response.__dict__


@router.delete('/remove/{employee_id}/', status_code=204)
async def remove_employee(employee_id: int, db: Session = Depends(get_db)): return delete_employee(db, employee_id)
