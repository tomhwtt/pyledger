from app.account import Account
from app.user import User


def test_transaction():
    user = User("tester", "tester@example.com")
    account = Account(user.id)

    tx1 = account.deposit(100)
    tx2 = account.withdraw(50)

    assert account.balance == 50.00
    assert tx1.type == "credit"
    assert tx2.type == "debit"
