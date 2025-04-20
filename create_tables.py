from pyledger.db import engine, Base
from pyledger.adapters.orm import UserModel, AccountModel

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created")

if __name__ == "__main__":
    create_tables()
