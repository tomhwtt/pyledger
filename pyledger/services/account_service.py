from pyledger.domain.account import Account
from pyledger.repository.account_repository import AbstractAccountRepository


class AccountService:
    def __init__(self, account_repository: AbstractAccountRepository):
        self.repo = account_repository

    def create_account(self, owner: str) -> Account:
        account = Account.create(owner=owner)
        self.repo.add(account)
        return account
