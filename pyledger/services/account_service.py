from uuid import UUID
from typing import List
from pyledger.domain.account import Account
from pyledger.repository.account_repository import AbstractAccountRepository


class AccountService:
    def __init__(self, account_repository: AbstractAccountRepository):
        self.repo = account_repository

    def create_account(self, owner_id: UUID) -> Account:
        account = Account.create(owner_id=owner_id)
        self.repo.add(account)
        return account

    def get_accounts_for_user(self, user_id: UUID) -> List[Account]:
        return self.repo.get_by_user_id(user_id)
