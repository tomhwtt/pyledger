import uuid
from app.user import User


def test_user_dict_returns_expected_values():
    user = User("tester", "tester@example.com")
    user_dict = user.to_dict()
    uuid_obj = uuid.UUID(user_dict["id"])

    assert user_dict["username"] == "tester"
    assert user_dict["email"] == "tester@example.com"
    assert str(uuid_obj) == user_dict["id"]
