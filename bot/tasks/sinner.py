"""
One who sins or lives in disregard of ceremonial prescription.

He repents his sins by helping this app with timetable scraping.
"""
from typing import Optional
from datetime import date

from .scraper.timetable.timetable_scraper import get_timetable, TimetableType
from .scraper.timetable.lesson_printer import LessonPrinter
from .time_manager import get_next_lesson

class Sinner:
    def __init__(self, user):
        self.user = user

    def handle(self, task: str, entity) -> str:
        """Returns a human-readable representation of the timetable."""
        if entity == None:
            if self.user.cl != None:
                entity = self.user.cl
            else:
                self.user.state = "entity"
                return "A jakou máš třídu?"
        elif task == "current":
            timetable = get_timetable(entity, TimetableType.Current)
            lesson_printer = LessonPrinter(timetable)
            output = lesson_printer.get_week()
            if output == "":
                output = "Žádný rozvrh."
            return output
        elif task == "next":
            timetable = get_timetable(entity, TimetableType.NextWeek)
            lesson_printer = LessonPrinter(timetable)
            output = lesson_printer.get_week()
            if output == "":
                output = "Žádný rozvrh."
            return output
        elif task == "permanent":
            timetable = get_timetable(entity, TimetableType.Permanent)
            lesson_printer = LessonPrinter(timetable)
            output = lesson_printer.get_week(day)
            if output == "":
                output = "Žádný rozvrh."
            return output
        elif task == "changes":
            timetable = get_timetable(entity, TimetableType.Current)
            lesson_printer = LessonPrinter(timetable)
            output = lesson_printer.get_week(only_changes=True)
            if output == "":
                output = "Žádné změny."
            return output
        elif task == "lesson":
            timetable = get_timetable(entity, TimetableType.Current)
            lesson_printer = LessonPrinter(timetable)
            day = date.today().weekday()
            lesson = get_next_lesson()
            if lesson >= 10:
                day += 1
                lesson = 0
            if day >= 5:
                day = lesson = 0
            output = lesson_printer.get_lesson(day, lesson,
                    include_teacher=Ture, include_theme=True)
            if output == "":
                output = "Příští hodinu je volno."
            return output
        elif task == "homework":
            # Would be great to add this feature.
            return "Máš štěstí, v bakalářích nic nevidím."
        else:
            current_day = date.today().weekday()
            day = self.get_day(current_day, task)
            timetable_type = TimetableType.NextWeek if day < current_day else TimetableType.Current
            timetable = get_timetable(entity, timetable_type)
            lesson_printer = LessonPrinter(timetable)
            output = lesson_printer.get_day(day)
            if output == "":
                output = "Žádný rozvrh."
            return output

    def get_day(self, current_day: int, task: str) -> int:
        """Returns the day in week index according to current day and given task."""
        if task[0] == "+":
            day = current_day + int(task[1])
            if day > 4:
                return 0
            return day
        return int(task[0])
