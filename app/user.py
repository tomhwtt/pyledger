import uuid


class User:
    def __init__(self, username: str, email: str):
        self.id = str(uuid.uuid4())
        self.username = username
        self.email = email

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email}

    def __str__(self):
        return f"User: {self.username} -> {self.id}"
