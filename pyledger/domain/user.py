import uuid


class User:
    def __init__(self, username: str, email: str, id: str = None):
        self.id = id or str(uuid.uuid4())
        self.username = username
        self.email = email

    @classmethod
    def create(cls, username: str, email: str) -> "User":
        return cls(username=username, email=email)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email}

    def __str__(self):
        return f"User: {self.username} -> {self.id}"
