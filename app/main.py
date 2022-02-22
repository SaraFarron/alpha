from fastapi import FastAPI
from database import engine
from routers import router
from models import Base


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router)
