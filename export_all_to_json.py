import sqlite3
import json
import os

def export_db_to_json(db_path, output_name=None):
    if not os.path.exists(db_path):
        print(f"Skipping {db_path} (file not found)")
        return

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # rows -> dict easily
    cur = conn.cursor()

    # get all tables
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cur.fetchall()]

    data = {}
    for table in tables:
        cur.execute(f"SELECT * FROM {table}")
        rows = [dict(r) for r in cur.fetchall()]
        data[table] = rows

    if output_name is None:
        output_name = os.path.splitext(os.path.basename(db_path))[0]

    out_file = f"{output_name}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    conn.close()
    print(f"Exported {db_path} -> {out_file}")

if __name__ == "__main__":
    # main resume + AI analysis DB
    export_db_to_json("resume_data.db", "resume_data_export")

    # feedback DB
    export_db_to_json(os.path.join("feedback", "feedback.db"), "feedback_export")
