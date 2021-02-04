from db import DB
from .czert_handler import CzertHandler
from typing import Optional
import re

class DevilBot:
    def __init__(self, path, teachers, classes):
        self.model = CzertHandler()
        self.database = DB(path)
        self.teachers = teachers
        self.classes = classes

    def answer(self, question: str, threshold = -10) -> str:
        """
        Returns the most similar question from the list to the given one.
        If none of these reach the [threshold] similarity, None is returned.
        If the threshold is not provided None is never returned.
        """
        key = self.model.get_closest_question([key for key in
            self.database.queries()], question, threshold)
        print(f"key: {key}")
        ans = self.database[key]
        return ans
    
# The following methods are temporarily not typed as the classes are in completely different folder.
# ?
# ??

    def get_closest_entity(self, question: str):
        """
        Returns the class or the teacher probably mentioned in the question.
        If it appears that no class or teacher was mentioned, returns None.
        """
        output = self.get_closest_class(question)
        if output is None:
            if self._nonexisting_class(question):
                return "wrong"
        # Tries to find teacher if search for class failed.
            else:
                output = self.get_closest_teacher(question)
        return output


    def _nonexisting_class(self, question: str) -> bool:
        """ Checks if the question contains class that does not exist. """
        match = re.search("[1-9]\.? ?[a-zA-Z]", question)
        return match is not None


    def get_closest_class(self, question: str):
        """
        Returns the class probably mentioned in the question.
        If it appears that no class was mentioned, returns None.
        """
        match = re.search("[1-8]\.? ?[a-cA-ceE]", question)
        if match == None:
            return None
        match = match.group(0)
        match = match.replace(" ","")
        if len(match) == 2:
            match = match[0] + "." + match[1]
        match = match.upper()
        if match in self.classes.classes_from_name:
            return self.classes.classes_from_name[match]
        return None

    def get_closest_teacher(self, question: str):
        """
        Returns the teacher probably mentioned in the question.
        If it appears that no class was mentioned, returns None.
        """
        # The threshold probably needs an adjustment.
        threshold = 2.0
        teacher_name = self.model.get_closest_question([teacher.full_name
            for teacher in self.teachers.teachers],
            question, threshold)
        if teacher_name is None:
            return None
        return self.teachers.teachers_from_name[teacher_name]

    def get_number(self, question: str) -> Optional[int]:
        """Returns the number it sees in the question."""
        q = question.lower()
        if "10" in q or "desát" in q or "desat" in q:
            return 9
        if "1" in q or "prvn" in q:
            return 0
        if "2" in q or "druh" in q:
            return 1
        if "3" in q or "tret" in q or "třet" in q:
            return 2
        if "4" in q or "čtvrt" in q or "ctvrt" in q:
            return 3
        if "5" in q or "pát" in q or "pat" in q:
            return 4
        if "6" in q or "šest" in q  or "sest":
            return 5
        if "7" in q or "sedm" in q:
            return 6
        if "8" in q or "osm" in q:
            return 7
        if "9" in q or "devát" in q  or "devat" in q:
            return 8

        





