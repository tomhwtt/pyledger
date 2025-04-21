from sqlalchemy.orm import Session
from pyledger.domain.transaction import Transaction
from pyledger.repository.transaction_repository import AbstractTransactionRepository
from pyledger.adapters.orm import TransactionModel


class TransactionSqlAlchemyRepository(AbstractTransactionRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, transaction: Transaction) -> None:
        transaction_model = TransactionModel.from_domain(transaction)
        self.session.add(transaction_model)

    def get_by_id(self, id: str) -> Transaction | None:
        row = self.session.query(TransactionModel).filter_by(id=id).first()
        return row.to_domain() if row else None
