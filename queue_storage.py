"""SQLite storage helpers for the work queue."""

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Any


DATABASE_FILE = Path(__file__).with_name("work_queue.db")


@contextmanager
def _connection():
    connection = sqlite3.connect(DATABASE_FILE, timeout=10)
    try:
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA journal_mode = WAL")
        connection.execute("PRAGMA busy_timeout = 10000")
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS jobs (
                id TEXT PRIMARY KEY,
                description TEXT NOT NULL,
                status TEXT NOT NULL CHECK (
                    status IN ('pending', 'in_progress', 'done')
                ),
                created_at TEXT NOT NULL,
                consumer_pid INTEGER,
                started_at TEXT,
                finished_at TEXT
            )
            """
        )
        connection.commit()
        yield connection
    finally:
        connection.close()


def add_jobs(jobs: list[dict[str, Any]]) -> None:
    """Add pending jobs to the queue."""
    with _connection() as connection:
        connection.executemany(
            """
            INSERT INTO jobs (id, description, status, created_at)
            VALUES (:id, :description, :status, :created_at)
            """,
            jobs,
        )
        connection.commit()


def claim_job(consumer_pid: int, started_at: str) -> dict[str, Any] | None:
    """Atomically claim the oldest pending job."""
    with _connection() as connection:
        connection.execute("BEGIN IMMEDIATE")
        row = connection.execute(
            """
            SELECT id, description, status, created_at, consumer_pid,
                   started_at, finished_at
            FROM jobs
            WHERE status = 'pending'
            ORDER BY rowid
            LIMIT 1
            """
        ).fetchone()

        if row is None:
            connection.rollback()
            return None

        connection.execute(
            """
            UPDATE jobs
            SET status = 'in_progress',
                consumer_pid = ?,
                started_at = ?
            WHERE id = ? AND status = 'pending'
            """,
            (consumer_pid, started_at, row["id"]),
        )
        connection.commit()

        job = dict(row)
        job["status"] = "in_progress"
        job["consumer_pid"] = consumer_pid
        job["started_at"] = started_at
        return job


def complete_job(job_id: str, finished_at: str) -> None:
    """Mark a claimed job as completed."""
    with _connection() as connection:
        cursor = connection.execute(
            """
            UPDATE jobs
            SET status = 'done', finished_at = ?
            WHERE id = ? AND status = 'in_progress'
            """,
            (finished_at, job_id),
        )
        if cursor.rowcount != 1:
            raise RuntimeError(f"job {job_id} is missing or not in progress")
        connection.commit()


def read_jobs() -> list[dict[str, Any]]:
    """Return all jobs, ordered by insertion order."""
    with _connection() as connection:
        rows = connection.execute(
            """
            SELECT id, description, status, created_at, consumer_pid,
                   started_at, finished_at
            FROM jobs
            ORDER BY rowid
            """
        ).fetchall()
    return [dict(row) for row in rows]
