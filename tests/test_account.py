import datetime
import uuid
import pytest
from app.user import User
from app.account import Account
from app.exceptions import InsufficientFundsError


def test_user_dict_returns_expected_values():
    user = User("tester", "tester@example.com")
    account = Account(user.id)
    account_dict = account.to_dict()
    uuid_obj = uuid.UUID(account_dict["id"])

    assert account_dict["owner"] == user.id
    assert account_dict["balance"] == 0
    assert isinstance(account_dict["created_at"], datetime.datetime)
    assert str(uuid_obj) == account_dict["id"]


def test_deposit_updates_balance_as_expected():
    user = User("tester", "tester@example.com")
    account = Account(user.id)
    account.deposit(100.00)

    assert account.balance == 100.00


def test_withdraw_updates_balance_as_expected():
    user = User("tester", "tester@example.com")
    account = Account(user.id)
    account.deposit(100.00)
    account.withdraw(50.00)

    assert account.balance == 50.00


def test_deposit_raises_value_error_if_amount_zero():
    user = User("tester", "tester@example.com")
    account = Account(user.id)

    with pytest.raises(ValueError):
        account.deposit(0)


def test_withdraw_raises_value_error_if_amount_zero():
    user = User("tester", "tester@example.com")
    account = Account(user.id)

    with pytest.raises(ValueError):
        account.withdraw(0)


def test_withdraw_more_than_balance_raises_insufficient_funds():
    user = User("tester", "tester@example.com")
    account = Account(user.id)
    account.deposit(100.00)

    with pytest.raises(InsufficientFundsError):
        account.withdraw(101.00)
