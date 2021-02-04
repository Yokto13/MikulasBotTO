from .models.lesson import Lesson
from typing import List

class LessonPrinter:
    """Class providing a pretty representaion of the timetable."""
    def __init__(self, timetable: List[List[List[Lesson]]]):
        self.timetable = timetable
    
    days_in_week = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek"]
    lesson_times = {
            1 : "8:00 — 8:45",
            2 : "8:50 — 9:35",
            3 : "9:55 — 10:40",
            4 : "10:45 — 11:30",
            5 : "11:40 — 12:25",
            6 : "12:30 — 13:15",
            7 : "13:05 — 13:50",
            8 : "13:55 — 14:40",
            9 : "14:50 — 15:35",
            10 : "15:40 — 16:25",
            }
    
    def nonempty_lesson(self, day: int, lesson: int, only_changes: bool) -> bool:
        """Determines if the lesson is empty or not."""
        return len(list(filter(lambda x: x.change or not only_changes,
            self.timetable[day][lesson]))) > 0

    def nonempty_day(self, day: int, only_changes: bool) -> bool:
        """Determines if the day is empty or not."""
        for i in range(len(self.timetable[day])):
            if self.nonempty_lesson(day, i, only_changes):
                return True
        return False
    
    def get_week(self, only_changes: bool = False, include_teacher:bool = False,
            include_theme: bool = False, include_groups: bool = False) -> bool:
        """Returns formated string representing the timetable for the whole week."""
        return "\n".join([
            self.get_day(day, only_changes, include_teacher,include_theme, include_groups)
            for day in range(5)
            if self.nonempty_day(day, only_changes)
            ])

    def get_day(self, day: int, only_changes: bool = False, include_teacher: bool = False,
            include_theme: bool = False, include_groups: bool = False) -> bool:
        """Returns formated string representing the timetable for a given day."""
        return f"{self.days_in_week[day]}:\n" + "".join([
            self.get_lesson(day, i, only_changes, include_teacher,
                include_theme, include_groups)
            for i in range(10)
            if self.nonempty_lesson(day, i, only_changes)
            ])

    def get_lesson(self, day: int, lesson: int, only_changes: bool = False,
            include_teacher: bool = False, include_theme: bool = False,
            include_groups: bool = False) -> bool:
        """Returns formated string representing the lessons at a given time on a given day."""
        return  f"{self.lesson_times[lesson + 1]}:\n" + "".join([
            self._get_concrete_lesson(day, lesson, i, include_teacher,
                include_theme, include_groups)
            for i in range(len(self.timetable[day][lesson]))
            if not only_changes or self.timetable[day][lesson][i].change
            ])
            
    def _get_concrete_lesson(self, day: int, lesson_index: int, concrete_lesson: int,
            include_teacher: bool, include_theme: bool, include_groups: bool) -> bool:
        """Returns formated string representing the concrete lesson."""
        lesson = self.timetable[day][lesson_index][concrete_lesson]
        output = f"  {lesson.name}"
        if lesson.classroom != "":
            output += f", učebna: {lesson.classroom}"
        if include_groups and lesson.groups != [] and lesson.groups != None and lesson.groups[0] != "":
            output += ", skupiny: " + " + ".join(lesson.groups)
        if include_teacher and lesson.teacher != "":
            output += f", učitel: {lesson.teacher}"
        if include_theme and lesson.theme != "":
            output += f", téma: {lesson.theme}"
        output += "\n"
        return output

