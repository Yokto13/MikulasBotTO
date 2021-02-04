from dataclasses import dataclass

@dataclass
class Teacher:
    """Class storing information about a teacher."""
    first_name: str
    second_name: str
    full_name: str
    abbreviation: str
    email: str
    phone: str
    room: str
    url: str

