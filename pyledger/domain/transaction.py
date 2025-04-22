import datetime
import uuid
from uuid import UUID
from enum import Enum


class TransactionType(str, Enum):
    CREDIT = "credit"
    DEBIT = "debit"


class Transaction:
    def __init__(self, account_id: UUID, type: str, amount: float):
        self.id = uuid.uuid4()
        self.account_id = account_id
        self.type = type
        self.amount = amount
        self.created_at = datetime.datetime.now()

    @classmethod
    def create(cls, account_id: UUID, type: TransactionType, amount: float):
        if not isinstance(type, TransactionType):
            raise ValueError("Transaction type must be a TransactionType enum")
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return cls(account_id=account_id, type=type, amount=amount)

    @classmethod
    def reconstruct(
        cls,
        id: UUID,
        account_id: UUID,
        type: TransactionType,
        amount: float,
        created_at: datetime.datetime,
    ) -> "Transaction":
        transaction = cls(account_id, type, amount)
        transaction.id = id
        transaction.created_at = created_at
        return transaction

    def to_dict(self):
        return {
            "id": self.id,
            "account_id": self.account_id,
            "type": self.type,
            "amount": self.amount,
            "created_at": self.created_at,
        }

    def __str__(self):
        return f"{self.type} -> ${self.amount}"
