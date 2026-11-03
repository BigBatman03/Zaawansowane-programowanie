"""Add work items to the file-backed queue."""

import argparse
from datetime import datetime, timezone
from uuid import uuid4

from queue_storage import QUEUE_FILE, queue_lock, read_jobs, write_jobs


def create_jobs(count: int):
    """Create pending jobs with unique identifiers."""
    created_at = datetime.now(timezone.utc).isoformat()
    return [
        {
            "id": str(uuid4()),
            "description": f"Phone call #{number}",
            "status": "pending",
            "created_at": created_at,
        }
        for number in range(1, count + 1)
    ]


def main():
    parser = argparse.ArgumentParser(description="Add jobs to the work queue.")
    parser.add_argument(
        "count",
        nargs="?",
        type=int,
        default=100,
        help="number of jobs to add (default: 100)",
    )
    args = parser.parse_args()

    if args.count < 1:
        parser.error("count must be at least 1")

    jobs = create_jobs(args.count)
    with queue_lock():
        current_jobs = read_jobs()
        write_jobs(current_jobs + jobs)

    print(f"Added {len(jobs)} pending jobs to {QUEUE_FILE}")


if __name__ == "__main__":
    main()
