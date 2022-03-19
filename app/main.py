from fastapi import FastAPI
from starlette.responses import RedirectResponse

from database import engine
from routers import management, tasks, user
from models import Base

description = """
Alpha application is my first project using FastAPI. This application is some kind of management tool of
imaginable company. It has only API though.

### Here users are divided into three groups:

+ Employees - those who can receive and do tasks, that they were given
+ Managers - those, who can create and assign tasks to employees
+ Directors - those, who can remove employees or move user status (raise employee to manager e.g.) 

### Tech stack:

+ Authorisation - JWT
+ DB - postgres
+ ORM - SQLAlchemy
+ Migrations - Alembic
+ Deployment - Docker

"""

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title='Alpha app',
    description=description,
    version='1',
    contact={
        'name': 'Syulin Nikita (SaraFarron on GitHub)',
        'url': 'https://github.com/SaraFarron'
    },
    license_info={
        'name': 'Unilicense',
        'url': 'https://unlicense.org/'
    }
)
app.include_router(management.router)
app.include_router(tasks.router)
app.include_router(user.router)


@app.get('/', description='This endpoint just redirects to swagger docs')
async def index(): return RedirectResponse(url='/docs')
