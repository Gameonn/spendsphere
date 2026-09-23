import sqlite3
from datetime import date

import pytest
from werkzeug.security import check_password_hash

from database import db


@pytest.fixture(autouse=True)
def temp_db(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", str(tmp_path / "test.db"))


@pytest.fixture
def seeded():
    db.init_db()
    db.seed_db()


@pytest.fixture
def conn():
    connection = db.get_db()
    yield connection
    connection.close()


def test_tables_exist(conn):
    db.init_db()
    tables = {
        row["name"]
        for row in conn.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
    }
    assert {"users", "expenses"} <= tables


def test_init_db_is_idempotent():
    db.init_db()
    db.init_db()


def test_seed_db_runs_once(seeded, conn):
    db.seed_db()
    assert conn.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 1
    assert conn.execute("SELECT COUNT(*) FROM expenses").fetchone()[0] == 8
    categories = {row["category"] for row in conn.execute("SELECT category FROM expenses")}
    assert categories == set(db.CATEGORIES)


def test_seed_dates_in_current_month(seeded, conn):
    today = date.today()
    for row in conn.execute("SELECT date FROM expenses"):
        assert row["date"].startswith(today.strftime("%Y-%m-"))
        assert row["date"] <= today.isoformat()


def test_password_is_hashed(seeded, conn):
    user = conn.execute(
        "SELECT password_hash FROM users WHERE email = ?", ("demo@spendsphere.com",)
    ).fetchone()
    assert user["password_hash"] != "demo123"
    assert check_password_hash(user["password_hash"], "demo123")


def test_duplicate_email_rejected(seeded, conn):
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            ("Someone", "demo@spendsphere.com", "x"),
        )


def test_foreign_key_enforced(seeded, conn):
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO expenses (user_id, amount, category, date) VALUES (?, ?, ?, ?)",
            (9999, 10.0, "Food", date.today().isoformat()),
        )


def test_row_factory_is_row(seeded, conn):
    row = conn.execute("SELECT * FROM users").fetchone()
    assert isinstance(row, sqlite3.Row)
    assert row["email"] == "demo@spendsphere.com"
