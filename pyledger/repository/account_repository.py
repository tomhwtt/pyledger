from abc import ABC, abstractmethod
from uuid import UUID
from typing import List
from pyledger.domain.account import Account


class AbstractAccountRepository(ABC):

    @abstractmethod
    def add(self, account: Account) -> None:
        """Add an Account to the system."""
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Account | None:
        """Retrieve an Account by id."""
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: UUID) -> List[Account]:
        """Return all accounts belonging to a given user."""
        pass
