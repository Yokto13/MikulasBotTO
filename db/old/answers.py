from typing import Iterator

from random import choice
from .answer import Answer

class Answers:
    """ Class to store answers and provide methods for their retrivial. """
    def __init__(self):
        self._answers = []

    def add(self, answer: Answer):
        if isinstance(answer, Answer):
            self._answers.append(answer)
        else:
            raise TypeError

    def add_from_text(self, text: str):
        ans = Answer(text)
        self.add(ans)

    def print_answers(self): # Mainly for debug
        for a in self._answers:
            print(a.text)

    def __iter__(self) -> Iterator[Answer]:
        return iter(self._answers)

    def remove_answer_by_text(self, text: str):
        to_rm = -1
        for i, a in enumerate(self._answers):
            if a.text == text:
                to_rm = i
                break
        if to_rm != -1:
            self._answers.pop(to_rm)
        else:
            raise KeyError

    def random(self) -> str:
        return choice(self._answers).text

    def mood(self) -> str:
        raise NotImplementedError

