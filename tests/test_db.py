import pytest
from sqlalchemy import text
from app.db import SessionLocal


def test_database_connection():
    try:
        db = SessionLocal()
        result = db.execute(text("SELECT 1"))
        value = result.scalar()
        assert value == 1
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")
    finally:
        db.close()
