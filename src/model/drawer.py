from datetime import datetime


class Drawer:
    def __init__(self, id: int, locker_id: str, created_at: datetime) -> None:  # noqa: A002
        self.id = id
        self.locker_id = locker_id
        self.created_at = created_at
