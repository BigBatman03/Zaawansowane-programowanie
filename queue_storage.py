"""Shared storage helpers for the file-backed work queue."""

import json
import os
import time
from contextlib import contextmanager
from pathlib import Path
from uuid import uuid4


QUEUE_FILE = Path(__file__).with_name("work_queue.jsonl")
LOCK_FILE = QUEUE_FILE.with_suffix(".lock")


@contextmanager
def queue_lock(timeout: float = 10.0):
    """Lock queue operations across producer and consumer processes."""
    deadline = time.monotonic() + timeout
    lock_handle = None

    while lock_handle is None:
        try:
            lock_handle = LOCK_FILE.open("x", encoding="utf-8")
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise TimeoutError("could not acquire the queue lock")
            time.sleep(0.1)

    try:
        yield
    finally:
        lock_handle.close()
        try:
            LOCK_FILE.unlink()
        except FileNotFoundError:
            pass


def read_jobs():
    """Read all jobs from the queue file."""
    if not QUEUE_FILE.exists():
        return []

    jobs = []
    with QUEUE_FILE.open("r", encoding="utf-8") as queue_file:
        for line in queue_file:
            if line.strip():
                jobs.append(json.loads(line))
    return jobs


def write_jobs(jobs):
    """Atomically replace the queue file with the supplied jobs."""
    temporary_file = QUEUE_FILE.with_name(
        f".{QUEUE_FILE.name}.{os.getpid()}.{uuid4().hex}.tmp"
    )
    try:
        with temporary_file.open("w", encoding="utf-8") as queue_file:
            for job in jobs:
                queue_file.write(json.dumps(job, ensure_ascii=False) + "\n")
            queue_file.flush()
            os.fsync(queue_file.fileno())

        deadline = time.monotonic() + 2
        while True:
            try:
                temporary_file.replace(QUEUE_FILE)
                return
            except PermissionError:
                if time.monotonic() >= deadline:
                    raise
                time.sleep(0.01)
    finally:
        temporary_file.unlink(missing_ok=True)
