from app.db import engine, Base
from app.models import user_model


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created")


if __name__ == "__main__":
    create_tables()
