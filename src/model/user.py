from datetime import datetime
from typing import Literal

UserLostAndFoundState = Literal["NONE", "DELIVERING", "RETRIEVING"]


class User:
    def __init__(  # noqa: PLR0913
        self,
        id: str,  # noqa: A002
        auth_id: str,
        name: str,
        email: str,
        lost_and_found_state: UserLostAndFoundState,
        avatar_url: str,
        is_disclose_as_owner: bool,  # noqa: FBT001
        created_at: datetime,
    ) -> None:
        self.id = id
        self.auth_id = auth_id
        self.name = name
        self.email = email
        self.lost_and_found_state = lost_and_found_state
        self.avatar_url = avatar_url
        self.is_disclose_as_owner = is_disclose_as_owner
        self.created_at = created_at
