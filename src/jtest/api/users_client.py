import os
from typing import List

import requests

from jtest.model.user import User

USERS_API_HOST = os.getenv("USERS_API_HOST", "https://6390b67465ff4183111c8926.mockapi.io")


class UsersClient:
    """ Client for Users API """

    def __init__(self, host: str = USERS_API_HOST) -> None:
        self.host = host

    def get_users(self, timeout: int = 5, **kwargs) -> List[User]:
        """ Obtains list of users via API

        Args:
            timeout: timeout in s for the API call
            **kwargs: requests kwargs

        Returns:
            List of users

        """
        response = requests.get(url=f"{self.host}/api/v1/user", timeout=timeout, **kwargs)
        response.raise_for_status()
        return [User(id=item["id"], name=item["name"]) for item in response.json()]

    def get_user(self, user_id: int) -> User:
        """ Obtains user details

        Args:
            user_id: ID of the user

        Returns:
            User

        """
        raise NotImplementedError("User endpoint is not yet defined")
