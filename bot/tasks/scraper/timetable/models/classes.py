from .teachers import Teachers
from .school_class import SchoolClass
import csv

class Classes:
    def __init__(self, classes_path: str, teachers: Teachers):
        self._classes_path = classes_path
        self.classes = []
        self.classes_from_name = {}
        self.teachers = teachers
        self._init_classes()

    def _init_classes(self) -> None:
        """Loads the classes from the [_classes_path] file."""
        with open(self._classes_path) as data_file:
            data = csv.reader(data_file, delimiter=",")
            self.classes.clear()
            for row in data:
                school_class = SchoolClass(
                        name=row[0],
                        classroom=row[1],
                        class_teacher=self.teachers.teachers_from_abbreviation[row[2]],
                        url=row[3])
                self.classes.append(school_class)
                self.classes_from_name[row[0]] = school_class

