from utils import database
from sqlalchemy import text   # <-- ADD THIS IMPORT

def main():
    session = database.get_database_connection()
    try:
        # Wrap SQL in text(...)
        result = session.execute(text("SELECT 1")).scalar_one()
        print("DB connection OK, SELECT 1 ->", result)

        # List all tables
        tables = session.execute(
            text("SELECT name FROM sqlite_master WHERE type='table'")
        ).fetchall()

        print("\nTables found in resume_data.db:")
        for (name,) in tables:
            print(" -", name)

    finally:
        session.close()

if __name__ == "__main__":
    main()
