from typing import NamedTuple

class Message(NamedTuple):
    sender: str
    text: str
    time_sent: float
    title: str
