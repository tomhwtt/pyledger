from sqlalchemy.orm import Session
from pyledger.domain.user import User
from pyledger.repository.user_repository import AbstractUserRepository
from pyledger.adapters.orm import UserModel


class UserSqlAlchemyRepository(AbstractUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, user: User) -> None:
        user_model = UserModel.from_domain(user)
        self.session.add(user_model)

    def get_by_email(self, email: str) -> User | None:
        row = self.session.query(UserModel).filter_by(email=email).first()
        return row.to_domain() if row else None
