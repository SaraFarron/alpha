from fastapi import FastAPI
import databases
import os
from database import SessionLocal, engine
import models
import schemas

database = databases.Database(os.environ.get('DATABASE_URL', "postgresql://postgres:postgres@postgresserver/db"))
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
async def root(): return {'message': 'Hello World!'}
