import sqlite3

DB_PATH = "resume_data.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Make sure the admin table exists (safety)
cursor.execute("""
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Insert admin user
email = "admin@example.com"
password = "admin123"

try:
    cursor.execute(
        "INSERT INTO admin (email, password) VALUES (?, ?)",
        (email, password),
    )
    conn.commit()
    print("Admin user created:", email, "/", password)
except sqlite3.IntegrityError:
    print("Admin already exists with this email:", email)

conn.close()
