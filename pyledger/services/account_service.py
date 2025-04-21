from uuid import UUID
from decimal import Decimal
from typing import List
from pyledger.domain.account import Account
from pyledger.repository.account_repository import AbstractAccountRepository
from pyledger.repository.transaction_repository import AbstractTransactionRepository


class AccountService:
    def __init__(
        self,
        account_repository: AbstractAccountRepository,
        transaction_repository: AbstractTransactionRepository,
    ):
        self.repo = account_repository
        self.transaction_repo = transaction_repository

    def create_account(self, owner_id: UUID) -> Account:
        account = Account.create(owner_id=owner_id)
        self.repo.add(account)
        return account

    def get_by_id(self, account: str) -> Account | None:
        return self.repo.get_by_id(account)

    def get_accounts_for_user(self, user_id: UUID) -> List[Account]:
        return self.repo.get_by_user_id(user_id)

    def get_balance(self, account_id: UUID) -> Decimal:
        transactions = self.transaction_repo.get_by_account_id(account_id)
        balance = Decimal("0.00")
        for txn in transactions:
            if txn.type == "credit":
                balance += Decimal(str(txn.amount))
            elif txn.type == "debit":
                balance -= Decimal(str(txn.amount))
        return balance
