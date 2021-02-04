from timetable_scraper import get_timetable, TimetableType
from lesson_printer import LessonPrinter
from models.teachers import Teachers
from models.classes import Classes




teachers = Teachers("data/teachers.txt")
classes = Classes("data/classes.csv", teachers)
timetable = get_timetable(classes.classes_from_name["8.E"], TimetableType.Current)
lp = LessonPrinter(timetable)
print("8.E:")
print("Default:")
print(lp.get_week())
print("All:")
print(lp.get_week(include_teacher=True, include_theme=True))
print("Changes:")
print(lp.get_week(only_changes=True))
print("")
print("Petr Brousek:")
br_timetable = get_timetable(teachers.teachers_from_abbreviation["Br"], TimetableType.Current)
br_lp = LessonPrinter(br_timetable)
print("Default:")
print(br_lp.get_week(include_groups=True))
print("Changes:")
print(br_lp.get_week(only_changes=True))

