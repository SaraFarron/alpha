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
    'title': 'test title',
    'description': 'test description',
    'price': 100,
    'time_to_complete': '01:30:00',
}
TASK_RESPONSE = {
    "id": 1,
    "title": "test title",
    "description": "test description",
    "price": 100,
    "user_id": 1,
    "is_completed": False,
    "time_to_complete": "01:30:00",
}
USER_PAYLOAD = {
    'email': 'test@user.com',
    'password': 'testpassword',
}


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def register():
    payload = {
        'fullname': 'Test User',
        'email': 'test@user.com',
        'password': 'testpassword',
    }
    response = client.post('user/signup/', json=payload)
    return response


def test_new_user():
    response = register()
    assert response.status_code == 200
    assert response.json()['access_token']


def test_login():
    payload = USER_PAYLOAD
    response = client.post('user/login/', json=payload)
    assert response.status_code == 200
    access_token = response.json()['access_token']
    assert access_token
    USER_PAYLOAD['access_token'] = access_token


def test_create_task_for_user():
    auth = {'Authorization': 'Bearer ' + USER_PAYLOAD['access_token']}
    payload = TASK_PAYLOAD
    params = {'user_id': 1}
    response = client.post(
        '/tasks/',
        json=payload,
        headers=auth,
        params=params,
    )
    assert response.status_code == 201, f'{response.text}'
    data = response.json()
    assert data['title'] == 'test title'


def test_get_tasks():
    auth = {'Authorization': 'Bearer ' + USER_PAYLOAD['access_token']}
    response = client.get('/tasks/', headers=auth)
    assert response.status_code == 200, f'{response.text}'
    data = response.json()
    del data['datetime_received']
    del data['datetime_completed']
    assert data == [TASK_RESPONSE, ]


def test_get_task():
    auth = {'Authorization': 'Bearer ' + USER_PAYLOAD['access_token']}
    response = client.get('/tasks/1/', headers=auth)
    assert response.status_code == 200, f'{response.text}'
    data = response.json()
    assert data == TASK_RESPONSE


def test_update_task():
    auth = {'Authorization': 'Bearer ' + USER_PAYLOAD['access_token']}
    response = client.patch(
        '/tasks/1/',
        json={'description': 'update test'},
        headers=auth,
    )
    assert response.status_code == 200, f'{response.text}\n{response.request.headers}'
    data = response.json()
    assert data['description'] == 'update test'


def test_destroy_task():
    auth = {'Authorization': 'Bearer ' + USER_PAYLOAD['access_token']}
    response = client.delete('/tasks/1/', headers=auth)
    assert response.status_code == 204, f'{response.text}'
