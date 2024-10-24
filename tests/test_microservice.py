import pytest
from microservice import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_devops(client):
    headers = {
        'Content-Type': 'application/json',
        'X-Parse-REST-API-Key': '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c'
    }
    response = client.post('/DevOps', json={
        "message": "This is a test",
        "to": "Juan Perez",
        "from": "Rita Asturia",
        "timeToLifeSec": 45
    }, headers=headers)
    
    assert response.status_code == 200
    assert response.json == {"message": "Hello Juan Perez your message will be sent"}
