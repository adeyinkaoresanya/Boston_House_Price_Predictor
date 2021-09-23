import json
import pytest
from app import app as flask_app
from app import __process_input

def test_process_input():
    data = json.dumps(
        {"inputs": [[3.67822, 0.0, 18.10, 0.0, 0.770, 5.362, 96.2, 2.1036, 24.0, 666.0, 20.2, 380.79, 10.19]]})
    result = __process_input(data)
    assert hasattr(result, '__array__')

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(app, client):
    response = client.get('/')
    assert response.status_code == 200
    result = 'Welcome to the Boston House Prediction Page'
    assert response.get_data(as_text=True) == result

def test_predict(app, client):
    data = json.dumps(
        {"inputs":
            [[11.8123, 0.0, 18.1, 0.0, 0.718, 6.824,76.5, 1.794, 24.0, 666.0, 20.2, 48.45, 22.74],
            [5.82115, 0.0, 18.1, 0.0, 0.713, 6.513, 89.9, 2.8016, 24.0, 666.0, 20.2, 393.82, 10.29]]})
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    result = {"Predicted House Price(s)": [11.98326974177815, 20.141554997067512]}
    assert json.loads(response.get_data()) == result
