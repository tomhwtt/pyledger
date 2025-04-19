import datetime
import uuid


class Transaction:
    def __init__(self, account, type, amount):
        self.id = str(uuid.uuid4())
        self.account = account
        self.type = type
        self.amount = amount
        self.created = datetime.datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "account": self.account,
            "type": self.type,
            "amount": self.amount,
            "created": self.created,
        }

    def __str__(self):
        return f"{self.type} -> ${self.amount}"
