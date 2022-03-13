from fastapi.testclient import TestClient
from .main import app
from .routers import get_db
from .database import TestingSessionLocal

# TODO


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_create_employee():
    response = client.post('/employees',
                           json={'name': 'test_employee'})
    assert response.status_code == 201
    data = response.json()
    assert 'id' in data
    assert data['name'] == 'test_employee'


def test_get_employees():
    response = client.get('/employees')
    assert response.status_code == 200
    data = response.json()
    assert data['todo'] == 'todo'


def test_get_employee():
    response = client.get('/employee/{employee_id}')
    assert response.status_code == 200
    data = response.json()
    assert data['todo'] == 'todo'


def test_delete_employees():
    response = client.delete('/employee/{employee_id}')
    assert response.status_code == 204


def test_create_task_for_employee():
    response = client.post('/employees/{employee_id}/task/')
    assert response.status_code == 201
    assert response.json() == {'todo': 'create this'}


def test_get_tasks():
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.json() == {'todo': 'create this'}


def test_get_task():
    response = client.get('/task/{task_id}')
    assert response.status_code == 200
    assert response.json() == {'todo': 'create this'}


def test_update_task():
    response = client.patch('/task/{task_id}')
    assert response.status_code == 200
    assert response.json() == {'todo': 'create this'}


def test_destroy_task():
    response = client.delete('/task/{task_id}')
    assert response.status_code == 204
    assert response.json() == {'todo': 'create this'}
