import datetime
import uuid
from app.user import User
from app.account import Account


def test_user_dict_returns_expected_values():
    user = User("tester", "tester@example.com")
    account = Account(user.id)
    account_dict = account.to_dict()
    uuid_obj = uuid.UUID(account_dict["id"])

    assert account_dict["owner"] == user.id
    assert account_dict["balance"] == 0
    assert isinstance(account_dict["created_at"], datetime.datetime)
    assert str(uuid_obj) == account_dict["id"]
