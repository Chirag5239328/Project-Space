import sqlite3


def init_db(db_path: str):

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            record_id TEXT,
            rule_id TEXT,
            priority INTEGER,
            matched INTEGER,
            decision TEXT,
            timestamp TEXT
        )
        """
    )

    conn.commit()
    conn.close()


def get_connection(db_path: str):

    return sqlite3.connect(db_path)
