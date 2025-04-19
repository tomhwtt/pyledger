import datetime
import uuid
from app.user import User


class Account:
    def __init__(self, owner):
        self.id = str(uuid.uuid4())
        self.owner = owner
        self.balance = 0
        self.created_at = datetime.datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "owner": self.owner,
            "balance": self.balance,
            "created_at": self.created_at,
        }

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass
