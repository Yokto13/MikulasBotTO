from dataclasses import dataclass
@dataclass
class Mark:
    subject: str
    value: str
    weight: int
    type_: str
    caption: str
    time_added: float

    def to_string(self) -> str:
        """Returns a human-readible format of the mark."""
        output = f"{self.value} váhy {self.weight} z předmětu {self.subject}"
        if self.caption != "":
            output += " za " + self.caption
        return output
