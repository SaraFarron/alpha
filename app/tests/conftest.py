import pytest
from starlette.testclient import TestClient
from sqlalchemy.ext.declarative import declarative_base
from os import remove

from app import database
from app.main import app
from app.models import Base


@pytest.fixture(scope='module')
def client():  # maybe first create Base and then import models?
    Base.metadata.create_all(bind=database.test_engine)
    setattr(database, 'get_db', database.override_get_db)
    setattr(database, 'Base', Base)
    client = TestClient(app)
    yield client
    setattr(database, 'get_db', database.get_db)
    remove('..test.db')
