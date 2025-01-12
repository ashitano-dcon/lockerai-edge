from typing import Literal

import requests

from model.drawer import Drawer
from model.user import User


class APIClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def put_in_lost_item(self, user_id: str) -> Drawer:
        response = requests.post(
            self.base_url + "/drawers/put-in",
            {
                "userId": user_id,
            },
        ).json()
        if response.get("statusCode") and response.get("statusCode") != 200:  # noqa: PLR2004
            msg = f"Failed to put in lost item. cause: {response.get('message')}"
            raise Exception(msg)

        drawer = Drawer(
            response.get("id"),
            response.get("lockerId"),
            response.get("createdAt"),
        )

        return drawer

    def take_out_lost_item(self, user_id: str) -> Drawer:
        response = requests.post(
            self.base_url + "/drawers/take-out",
            {
                "userId": user_id,
            },
        ).json()
        if response.get("statusCode") and response.get("statusCode") != 200:  # noqa: PLR2004
            msg = f"Failed to take out lost item. cause: {response.get('message')}"
            raise Exception(msg)

        drawer = Drawer(
            response.get("id"),
            response.get("lockerId"),
            response.get("createdAt"),
        )

        return drawer

    def update_locker_status(
        self,
        locker_id: str,
        type: Literal["INFO", "ERROR", "WARN", "SUCCESS"],  # noqa: A002
        name: str,
        description: str,
    ) -> None:
        requests.post(
            self.base_url + f"/lockers/{locker_id}/status",
            {
                "type": type,
                "name": name,
                "description": description,
            },
        )

    def find_user(self, user_id: str) -> User | None:
        response = requests.get(self.base_url + f"/users/{user_id}").json()
        if response.get("statusCode") and response.get("statusCode") != 200:  # noqa: PLR2004
            print(f"User not found. user_id: {user_id}")
            return None

        user = User(
            response.get("id"),
            response.get("authId"),
            response.get("name"),
            response.get("email"),
            response.get("lostAndFoundState"),
            response.get("avatarUrl"),
            response.get("isDiscloseAsOwner"),
            response.get("createdAt"),
        )

        return user
