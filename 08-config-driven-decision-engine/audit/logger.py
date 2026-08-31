from datetime import datetime

from audit.db import get_connection


class AuditLogger:

    def __init__(self, db_path: str):

        self.db_path = db_path
        self.conn = get_connection(db_path)

    def log(
        self,
        record_id: str,
        rule_id: str,
        priority: int,
        matched: bool,
        decision: str | None,
    ):

        cur = self.conn.cursor()

        cur.execute(
            """
            INSERT INTO audit_log (
                record_id,
                rule_id,
                priority,
                matched,
                decision,
                timestamp
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                record_id,
                rule_id,
                priority,
                int(matched),
                decision,
                datetime.utcnow().isoformat(),
            ),
        )

        self.conn.commit()

    def close(self):

        self.conn.close()
