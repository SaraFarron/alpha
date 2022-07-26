from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..database import Base, get_db
from ..main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


TASK_PAYLOAD = {

}
USER_PAYLOAD = {

}


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_create_task_for_user():
    response = client.post('/tasks/', json={'title': 'test_task', 'description': 'test_desc', 'time_to_complete': '00:10:00'})
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == 'test_task'


def test_get_tasks():
    response = client.get('/tasks')
    assert response.status_code == 200
    data = response.json()
    assert data == {'todo': 'create this'}


def test_get_task():
    response = client.get('/tasks/1')
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == 'test_task'


def test_update_task():
    response = client.patch('/tasks/1',
                            json={'is_completed': 'True'})
    assert response.status_code == 200
    data = response.json()
    assert data['is_completed'] == 'True'


def test_destroy_task():
    response = client.delete('/tasks/1')
    assert response.status_code == 204
