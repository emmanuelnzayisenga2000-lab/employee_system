import json
from app import app

def test_list_employees():
    client = app.test_client()
    resp = client.get('/employees')
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert isinstance(data, list)

def test_post_employee():
    client = app.test_client()
    payload = {"first_name": "Test", "last_name": "User", "role": "QA"}
    resp = client.post('/employees', json=payload)
    assert resp.status_code == 201
    data = json.loads(resp.data)
    assert data['first_name'] == 'Test'
    assert data['last_name'] == 'User'
