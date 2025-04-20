from abc import ABC, abstractmethod
from pyledger.domain.account import Account


class AbstractAccountRepository(ABC):

    @abstractmethod
    def add(self, account: Account) -> None:
        """Add an Account to the system."""
        pass
