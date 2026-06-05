"""Database utilities using built-in sqlite3 for PashuCare AI."""

import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "detections.db")


def get_connection():
    """Return a new sqlite3 connection with row_factory set."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create the detections table if it does not exist."""
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS detections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            disease_id INTEGER NOT NULL,
            disease_name TEXT NOT NULL,
            confidence INTEGER NOT NULL,
            severity TEXT NOT NULL,
            image_path TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def save_detection(user_id: str, disease_id: int, disease_name: str,
                   confidence: int, severity: str, image_path: str):
    """Insert a detection record and return its id."""
    conn = get_connection()
    cursor = conn.execute(
        """INSERT INTO detections
           (user_id, disease_id, disease_name, confidence, severity, image_path, timestamp)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (user_id, disease_id, disease_name, confidence, severity,
         image_path, datetime.utcnow().isoformat())
    )
    conn.commit()
    row_id = cursor.lastrowid
    conn.close()
    return row_id


def get_user_detections(user_id: str):
    """Return all detections for a given user, newest first."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM detections WHERE user_id = ? ORDER BY timestamp DESC",
        (user_id,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]
