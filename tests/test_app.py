# test_app.py
import requests
import pytest

@pytest.mark.parametrize("endpoint", ["/tests/test2/test.backup"])
def test_hello_endpoint(endpoint):
    url = f"http://localhost:5000{endpoint}"
    response = requests.get(url)
    data = response.json()
    assert response.status_code == 200
    assert 'content' in data
    assert data['content'] == 'hello it works'
