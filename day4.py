import json
import time
from collections.abc import Generator
from contextlib import contextmanager
from dataclasses import asdict
from datetime import date

from day3 import StudySession


@contextmanager
def track_session(subject: str) -> Generator[list[str], None, None]:
    start = time.time()
    topics: list[str] = []

    yield topics

    elapsed = max(1, int((time.time() - start) / 60))
    d = date.today()
    session = StudySession(subject, elapsed, d, topics)
    with open(f"{subject}_{d}.json", "w") as f:
        json.dump(asdict(session), f, default=str)


with track_session("Python") as topics:
    topics.append("context managers")
    topics.append("contextlib")
