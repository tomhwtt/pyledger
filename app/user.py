import uuid


class User:
    def __init__(self, username: str, email: str):
        self.id = str(uuid.uuid4())
        self.username = username
        self.email = email

    def __str__(self):
        return f"User: {self.username} -> {self.id}"
