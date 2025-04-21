import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from pyledger.db import Base
from pyledger.domain.user import User
from pyledger.domain.account import Account


class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    def to_domain(self) -> User:
        return User(id=self.id, username=self.username, email=self.email)

    @staticmethod
    def from_domain(user: User) -> "UserModel":
        return UserModel(id=user.id, username=user.username, email=user.email)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"


class AccountModel(Base):
    __tablename__ = "accounts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    balance = Column(Float, nullable=False, default=0.00)
    created_at = Column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    def to_domain(self) -> Account:
        return Account.reconstruct(
            id=self.id,
            owner_id=self.owner_id,
            balance=self.balance,
            created_at=self.created_at,
        )

    @staticmethod
    def from_domain(account: Account) -> "AccountModel":
        return AccountModel(
            id=account.id,
            owner_id=account.owner_id,
            balance=account.balance,
            created_at=account.created_at,
        )

    def __repr__(self):
        return f"<Account(id={self.id}, owner_id={self.owner_id})>"
