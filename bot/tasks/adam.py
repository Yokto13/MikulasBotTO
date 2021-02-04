"""
    As the first human, Adam provides information
    about those descents who were couragious enough
    to become teachers and about groups of innocent
    children who see their courage every day.
"""

from .scraper.timetable.models.teacher import Teacher


class Adam:
    def __init__(self, teachers, classes):
        self.teachers = teachers
        self.classes = classes
        self.non_teacher_tasks = ["classteacher", "stemroom"]

    def handle(self, task, entity):
        """Returns answers to queries concerned about teachers and classes."""
        if entity == None or (task in self.non_teacher_tasks and type(entity) is Teacher):
            if self.user.cl != None:
                entity = self.user.cl
            else:
                self.user.ask_devil = False
                return "A jakou máš třídu?"
        if task == "classteacher":
            return f"Třídní učitel {entity.name} je {entity.class_teacher.full_name}."
        elif task == "stemroom":
            return f"Kmenová třída {entity.name} je {entity.classroom}."
        else:
            if type(entity) is not Teacher:
                entity = entity.class_teacher
            if task == "phone":
                return "{entity.full_name} má telefonní číslo {entity.phone}."
            elif task == "email":
                return "{entity.full_name} má email {entity.email}."
            elif task == "room":
                return "{entity.full_name} má kabinet v místnosti {entity.room}."

