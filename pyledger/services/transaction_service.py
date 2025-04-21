from pyledger.domain.transaction import Transaction
from pyledger.repository.transaction_repository import AbstractTransactionRepository


class TransactionService:
    def __init__(self, transaction_repository: AbstractTransactionRepository):
        self.repo = transaction_repository

    def create_transaction(self, account: str, type: str, amount: float) -> Transaction:
        transaction = Transaction.create(account=account, type=type, amount=amount)
        self.repo.add(transaction)
        return transaction

    def get_by_id(self, transaction: str) -> Transaction | None:
        return self.repo.get_by_id(transaction)
