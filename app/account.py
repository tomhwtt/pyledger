import datetime
import threading
import uuid
from app.exceptions import InsufficientFundsError


class Account:
    def __init__(self, owner):
        self.id = str(uuid.uuid4())
        self.owner = owner
        self.balance = 0
        self.created_at = datetime.datetime.now()
        self._lock = threading.Lock()

    def to_dict(self):
        return {
            "id": self.id,
            "owner": self.owner,
            "balance": self.balance,
            "created_at": self.created_at,
        }

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")

        with self._lock:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")

        if self.balance - amount < 0:
            raise InsufficientFundsError("Insufficient Funds")

        with self._lock:
            self.balance -= amount
