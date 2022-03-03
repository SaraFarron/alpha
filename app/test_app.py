from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)
# TODO


def test_get_employees():
    response = client.get('/employees')
    assert response.status_code == 200
    assert response.json() == {'todo': 'create this'}


def test_get_employee():
    response = client.get('/employee/{employee_id}')
    assert response.status_code == 200
    assert response.json() == {'todo': 'create this'}


def test_create_employee():
    response = client.post('/employees')
    assert response.status_code == 200
    assert response.json() == {'todo': 'create this'}


def test_delete_employees():
    response = client.delete('/employee/{employee_id}')
    assert response.status_code == 200
    assert response.json() == {'todo': 'create this'}


def test_create_task_for_employee():
    response = client.post('/employees/{employee_id}/task/')
    assert response.status_code == 200
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
    response = client.get('/task/{task_id}')
    assert response.status_code == 200
    assert response.json() == {'todo': 'create this'}


def test_destroy_task():
    response = client.get('/task/{task_id}')
    assert response.status_code == 200
    assert response.json() == {'todo': 'create this'}
