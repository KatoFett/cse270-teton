import pytest
import requests
from requests_mock import Mocker

@pytest.fixture
def mock_requests_get(requests_mock):
    # Patching requests.get to return a mocked response
    requests_mock.get.return_value = MockResponse()

class MockResponse:
    def __init__(self, status_code=401):
        self.status_code = status_code

def test_endpoint(mock_requests_get):
    # Arrange
    url = "http://127.0.0.1:8000/users/"
    params = {
        "username": "admin",
        "password": "admin"
    }
    
    # Act
    response = requests.get(url, params=params)
    
    # Assert
    assert response.status_code == 401
