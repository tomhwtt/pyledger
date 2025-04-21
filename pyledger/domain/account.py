import datetime
import uuid
from uuid import UUID


class Account:
    def __init__(self, owner_id: UUID, id: UUID = None):
        self.id = id or uuid.uuid4()
        self.owner_id = owner_id
        self.created_at = datetime.datetime.now()

    @classmethod
    def create(cls, owner_id: UUID) -> "Account":
        return cls(owner_id=owner_id)

    @classmethod
    def reconstruct(
        cls,
        id: UUID,
        owner_id: UUID,
        created_at: datetime.datetime,
    ) -> "Account":
        account = cls(owner_id)
        account.id = id
        account.created_at = created_at
        return account

    def to_dict(self):
        return {
            "id": str(self.id),
            "owner_id": str(self.owner_id),
            "created_at": self.created_at.isoformat(),
        }
