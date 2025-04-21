from abc import ABC, abstractmethod
from uuid import UUID
from typing import List
from pyledger.domain.transaction import Transaction


class AbstractTransactionRepository(ABC):

    @abstractmethod
    def add(self, account: Transaction) -> None:
        """Add an Account to the system."""
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Transaction | None:
        """Retrieve a transaction by id."""
        pass

    @abstractmethod
    def get_by_account_id(self, account_id: UUID) -> List[Transaction]:
        """Return all transactions belonging to a given account."""
        pass
