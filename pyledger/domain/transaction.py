import datetime
import uuid
from uuid import UUID


class Transaction:
    def __init__(self, account: str, type: str, amount: float):
        self.id = str(uuid.uuid4())
        self.account = account
        self.type = type
        self.amount = amount
        self.created_at = datetime.datetime.now()

    @classmethod
    def create(cls, account: str, type: str, amount: float):
        return cls(account=account, type=type, amount=amount)

    @classmethod
    def reconstruct(
        cls,
        id: UUID,
        account: str,
        type: str,
        amount: float,
        created_at: datetime.datetime,
    ) -> "Transaction":
        transaction = cls(account, type, amount)
        transaction.id = id
        transaction.created_at = created_at
        return transaction

    def to_dict(self):
        return {
            "id": self.id,
            "account": self.account,
            "type": self.type,
            "amount": self.amount,
            "created_at": self.created_at,
        }

    def __str__(self):
        return f"{self.type} -> ${self.amount}"
