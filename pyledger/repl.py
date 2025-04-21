from sqlalchemy.orm import sessionmaker
from pyledger.db import engine
from pyledger.repository.user_sqlalchemy import UserSqlAlchemyRepository
from pyledger.repository.account_sqlalchemy import AccountSqlAlchemyRepository
from pyledger.repository.transaction_sqlalchemy import TransactionSqlAlchemyRepository
from pyledger.services.user_service import UserService
from pyledger.services.account_service import AccountService
from pyledger.services.transaction_service import TransactionService

Session = sessionmaker(bind=engine)
session = Session()

user_repo = UserSqlAlchemyRepository(session)
user_service = UserService(user_repo)

transaction_repo = TransactionSqlAlchemyRepository(session)
transaction_service = TransactionService(transaction_repo)

account_repo = AccountSqlAlchemyRepository(session)
account_service = AccountService(account_repo, transaction_repo)

print("REPL ready.")
