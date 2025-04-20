from sqlalchemy.orm import Session
from pyledger.domain.account import Account
from pyledger.repository.account_repository import AbstractAccountRepository
from pyledger.adapters.orm import AccountModel


class AccountSqlAlchemyRepository(AbstractAccountRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, account: Account) -> None:
        account_model = AccountModel.from_domain(account)
        self.session.add(account_model)
