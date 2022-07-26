from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

from database import get_db, SessionLocal
from auth import sign_jwt, Hasher
from crud import (
    get_all, create_entry, Session,
)
import schemas
import models

router = APIRouter(
    prefix='/user',
    tags=['user'],
)


def check_user(data: schemas.UserLoginSchema):
    users = get_all(SessionLocal(), models.User)
    for user in users:
        if user.email == data.email and Hasher.verify_password(data.password, user.password):
            return True
    return False


@router.post('/signup/', response_model=schemas.AccessToken)
async def signup(db: Session = Depends(get_db), user: schemas.UserSchema = Body(...)):
    hashed_password = Hasher.get_password_hash(user.password)
    user.password = hashed_password
    try:
        create_entry(db, models.User, user.dict())
    except IntegrityError as e:
        assert isinstance(e.orig, UniqueViolation)
        raise HTTPException(403, 'This username or email was already taken')
    return sign_jwt(user.email)


@router.post('/login/', response_model=schemas.AccessToken)
async def login(user: schemas.UserLoginSchema = Body(...)):
    if check_user(user):
        return sign_jwt(user.email)
    raise HTTPException(403, 'Login or password is incorrect')


@router.get('/', response_model=list[schemas.UserResponse])
async def all_users(db: Session = Depends(get_db)):
    return get_all(db, models.User)
