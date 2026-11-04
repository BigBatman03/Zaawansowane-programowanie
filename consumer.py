"""Continuously consume and execute jobs from the SQLite-backed queue."""

import argparse
import os
import time
from datetime import datetime, timezone

from queue_storage import claim_job as claim_queued_job
from queue_storage import complete_job as complete_queued_job


def claim_job():
    """Atomically change the first pending job to in_progress."""
    return claim_queued_job(
        consumer_pid=os.getpid(),
        started_at=datetime.now(timezone.utc).isoformat(),
    )


def complete_job(job_id: str):
    """Mark a job as done after its work has finished."""
    complete_queued_job(
        job_id=job_id,
        finished_at=datetime.now(timezone.utc).isoformat(),
    )


def consume_jobs(poll_interval: float, work_duration: float):
    """Poll forever, executing each claimed job for the configured duration."""
    print(
        f"Consumer {os.getpid()} started; polling every "
        f"{poll_interval:g}s"
    )
    while True:
        job = claim_job()
        if job is None:
            time.sleep(poll_interval)
            continue

        print(f"[{os.getpid()}] started {job['description']}")
        time.sleep(work_duration)
        complete_job(job["id"])
        print(f"[{os.getpid()}] completed {job['description']}")


def main():
    parser = argparse.ArgumentParser(description="Consume the work queue.")
    parser.add_argument(
        "--poll-interval",
        type=float,
        default=5,
        help="seconds between queue checks (default: 5)",
    )
    parser.add_argument(
        "--work-duration",
        type=float,
        default=30,
        help="seconds needed for one job (default: 30)",
    )
    args = parser.parse_args()

    if args.poll_interval <= 0 or args.work_duration < 0:
        parser.error(
            "poll interval must be positive and work duration non-negative"
        )
    consume_jobs(args.poll_interval, args.work_duration)


if __name__ == "__main__":
    main()
