from typing import List, Optional

from blacksheep import Response
from blacksheep.server.controllers import APIController, get, post


class UserAPIController(APIController):

    @classmethod
    def class_name(cls) -> str:
        return "users"

    @classmethod
    def version(cls) -> str:
        return "v1"

    @get()
    async def get_examples(self) -> List[str]:
        """
        Gets a list of caca.
        """
        return list(f"User {i}" for i in range(3))

    @get("{user_id}")
    def get_user(self, user_id: int) -> str:
        """Gets a cat by id."""
        return f"User {user_id}"


class UserAPIController(APIController):

    @classmethod
    def class_name(cls) -> str:
        return "users"

    @classmethod
    def version(cls) -> str:
        return "v2"

    @get()
    async def get_examples(self) -> List[str]:
        """
        Gets a list of best users examples.
        """
        return list(f"Best User  {i}" for i in range(3))

    @get("{user_id}")
    async def get_user(self, user_id: int) -> str:
        """Gets a cat by id."""
        return f"Best User {user_id}"
