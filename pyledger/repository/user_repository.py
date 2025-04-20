from abc import ABC, abstractmethod
from pyledger.domain.user import User


class AbstractUserRepository(ABC):

    @abstractmethod
    def add(self, user: User) -> None:
        """Add a user to the system."""
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        """Retrieve a user by their email, or return None."""
        pass
