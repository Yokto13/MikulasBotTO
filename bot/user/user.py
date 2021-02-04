from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    token: Optional[str] = None
    name: Optional[str] = None
    username: Optional[str] = None
    cl: Optional[str] = None
    state: str = ""
    last_task: Optional[str] = None
    vip: bool = False
