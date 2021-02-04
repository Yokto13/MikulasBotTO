from dataclasses import dataclass
from .teacher import Teacher

@dataclass
class SchoolClass:
    """Class storing information about a school class."""
    name: str
    url: str
    classroom: str
    class_teacher: Teacher

