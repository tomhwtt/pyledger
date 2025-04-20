from pyledger.domain.user import User
from pyledger.repository.user_repository import AbstractUserRepository


class UserService:
    def __init__(self, user_repository: AbstractUserRepository):
        self.repo = user_repository

    def register_user(self, username: str, email: str) -> User:
        if self.repo.get_by_email(email):
            raise ValueError("User with this email already exists.")

        user = User.create(username=username, email=email)
        self.repo.add(user)
        return user

    def get_user_by_email(self, email: str) -> User | None:
        return self.repo.get_by_email(email)
