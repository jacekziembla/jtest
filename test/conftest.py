import pytest
from jtest.api.users_client import UsersClient


@pytest.fixture
def init_api():
    """ Fixture initialising api clients """

    yield UsersClient()
