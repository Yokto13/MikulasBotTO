from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Lesson:
    """Class storing data about a lesson in the timetable."""
    name: str = ""
    teacher: str = ""
    classroom: str = ""
    homeworks: str = ""
    theme: str = ""
    groups: Optional[List[str]] = None 
    change: bool = False
   
