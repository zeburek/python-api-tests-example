import pytest

from api.client import RestfulBookerClient


@pytest.fixture(scope="session")
def client():
    client = RestfulBookerClient("https://restful-booker.herokuapp.com")
    client.authorize("admin", "password123")
    return client
