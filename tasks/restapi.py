#! python
import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="module")
def session():
    with requests.Session() as s:
        yield s

def test_get_post_returns_200(session):
    response = session.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_get_post_returns_json(session):
    response = session.get(f"{BASE_URL}/posts/1")
    assert response.headers["Content-Type"].startswith("application/json")

def test_get_post_has_expected_fields(session):
    data = session.get(f"{BASE_URL}/posts/1").json()
    assert "title" in data
    assert "body" in data

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])