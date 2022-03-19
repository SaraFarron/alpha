from fastapi import APIRouter, Depends, Body
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

from database import get_db, SessionLocal
from auth import sign_jwt
from crud import *
import schemas

router = APIRouter(
    prefix='/user',
    tags=['user'],
)


def check_user(data: schemas.UserLoginSchema):
    users = get_users(SessionLocal())
    for user in users:
        if user.email == data.email and Hasher.verify_password(data.password, user.password):
            return True
    return False


@router.post('/signup/')
async def signup(db: Session = Depends(get_db), user: schemas.UserSchema = Body(...)):
    try:
        new_user(db, user)
    except IntegrityError as e:
        assert isinstance(e.orig, UniqueViolation)
        raise HTTPException(403, 'This username or email was already taken')
    return sign_jwt(user.email)


@router.post('/login/')
async def login(user: schemas.UserLoginSchema = Body(...)):
    if check_user(user):
        return sign_jwt(user.email)
    raise HTTPException(403, 'Login or password is incorrect')