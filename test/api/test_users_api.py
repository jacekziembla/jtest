import pytest


@pytest.mark.api
class TestUserApi:
    """ Users API Suite """

    def test_get_users_endpoint(self, init_api) -> None:
        """ Verifies get users endpoint """

        expected_number_of_users = 65

        client = init_api
        users = client.get_users()

        assert len(users) == expected_number_of_users, "# of users does not match"

    def test_get_certain_user_endpoint(self, init_api):
        """ Verifies get certain user endpoint """

        user_id = 0
        client = init_api

        with pytest.raises(NotImplementedError) as exec_info:
            _ = client.get_user(user_id=user_id)

        assert str(exec_info.value) == "User endpoint is not yet defined", "The error is not thrown correctly"
