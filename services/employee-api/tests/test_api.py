import json
import os
from app import app, db, init_db


def setup_function():
    # Use an in-memory database for tests to avoid persisting state
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    with app.app_context():
        db.init_app(app)
        init_db(seed=True)


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
