"""
Romans 13:11

And do this, understanding the present time: 
The hour has already come for you to wake up from your slumber,
because our salvation is nearer now than when we first believed. 
"""

from typing import Optional
from datetime import datetime

_lesson_string = [
        "8:00 — 8:45",
        "8:50 — 9:35",
        "9:55 — 10:40",
        "10:45 — 11:30",
        "11:40 — 12:25",
        "12:30 — 13:15",
        "13:05 — 13:50",
        "13:55 — 14:40",
        "14:50 — 15:35",
        "15:40 — 16:25"]

_lesson_ranges = []  # To be inited.

def _convert_to_mins(hour: int, mins: int) -> int:
    return 60 * hour + mins


def _mins_from_bound(bound: str) -> int:
    return _convert_to_mins(
            int(bound.split(":")[0]),
            int(bound.split(":")[1])
            )

_lesson_ranges = [
        [_mins_from_bound(bound) for bound in human_readable.split("—")]
            for human_readable in _lesson_string
        ]


def get_next_lesson(hour: int = None, mins: int = None) -> int:
    """Returns the index of next lessing starting at 0."""
    current = _convert_to_mins(
            datetime.now().hour,
            datetime.now().minute
            )
    if hour is not None and mins is not None:
        current = _convert_to_mins(hour, mins)
    for i, r in enumerate(_lesson_ranges):
        if r[0] <= current <= r[1]:
            # Next after last is the first the next day.
            return (i + 1) % len(_lesson_ranges)
    return 0  # The first lesson.


def handle(lesson_index: Optional[int]) -> str:
    """Returns the time at which a given lesson starts and ends."""
    if lesson_index == None:
        lesson_index = get_next_lesson()
    return f"{lesson_index + 1}. hodina probíhá v čase: {_lesson_string[lesson_index]}."

