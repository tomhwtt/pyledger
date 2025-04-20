import datetime
import uuid


class Account:
    def __init__(self, owner: str, id: str = None):
        self.id = id or str(uuid.uuid4())
        self.owner = owner
        self.balance = 0
        self.created_at = datetime.datetime.now()

    @classmethod
    def create(cls, owner: str) -> "Account":
        return cls(owner=owner)

    def to_dict(self):
        return {
            "id": self.id,
            "owner": self.owner,
            "balance": self.balance,
            "created_at": self.created_at,
        }
