import requests
from .models.lesson import Lesson
from .models.school_class import SchoolClass
from .models.teacher import Teacher
from typing import List, Union
import enum

class TimetableType(enum.Enum):
    Current = 1
    NextWeek = 2
    Permanent = 3


_url_prefix = "https://bakalari.mikulasske.cz/Timetable/Public/"

def _type_to_string(t_type: TimetableType) -> str:
    """For the timetable type returns appropriate part in url."""
    if t_type == TimetableType.Current:
        return "Actual"
    elif t_type == TimetableType.NextWeek:
        return "Next"
    else: 
        return "Permanent"


def _get_url(t_type: TimetableType, model: Union[SchoolClass, Teacher]) -> str:
    """Returns url for the timetable of a given class or teacher."""
    model_type_url = ""
    if type(model) is Teacher:
        model_type_url = "/Teacher/"
    elif type(model) is SchoolClass:
        model_type_url = "/Class/"

    return _url_prefix + _type_to_string(t_type) + model_type_url + model.url


def _make_pretty(item: str) -> str:
    """Formats html code parts into nice strings."""
    item = item.replace(">", "")
    item = item.replace(":", "")
    item = item.replace("&quot;", "")
    item = item.replace("&#225;", "á")
    item = item.replace("&#237;", "í")
    item = item.replace("&#180;", "\'")
    item = item.replace("&#250;", "ú")
    item = item.replace("&#233;", "é")
    item = item.replace("Zruš", "Zrušeno")
    item =  item.strip()
    if item == "null":
        return ""
    return item


def _get_html(url: str) -> str:
    """Returns html code of the given url."""
    r = requests.get(url)
    return r.text


def _get_timetable(html: str) -> List[List[List[Lesson]]]:
    """Returns a timetable scraped from a given html code."""
    result = []
    index = html.find("body")
    for day in range(5):
        # Finds next day
        index = html.find("bk-timetable-row", index)
        result.append([])
        for i in range(10):
            # Finds next time for a lesson
            result[day].append([])
            index = html.find("bk-timetable-cell", index) + 1
            while html.find("bk-timetable-cell", index) > html.find("day-item-hover",
                    index) and html.find("day-item-hover", index) > index:
                # Finds next lesson in the given time
                index = html.find("day-item-hover", index)
                # Detects if there is a change in the current lesson
                change = html.find("h-100", index) < html.find("data-detail",
                        index) and html.find("h-100", index) > index
                # Searches for a theme
                theme = ""
                if html.find("theme", index) < html.find("top",
                        index) and html.find("theme", index) > index:
                    index = html.find("theme", index)
                    index = html.find(":", index)
                    theme_to = html.find(",", index)
                    theme = _make_pretty(html[index: theme_to])
                # Searches for groups
                index = html.find("left",index)
                index = html.find("<div>", index)
                groups_to = html.find("</div>", index)
                groups = html[index+5:groups_to].split("<br/>")
                for group_index in range(len(groups)):
                    groups[group_index] = groups[group_index].strip()
                # Searches for a classroom
                index = html.find("first", index)
                index = html.find(">", index)
                class_to = html.find("<", index)
                classroom = _make_pretty(html[index: class_to])
                # Searches for the subject"s shortcut
                index = html.find("middle", index)
                index = html.find(">", index)
                subject_to = html.find("<", index)
                subject = _make_pretty(html[index: subject_to])
                if subject == "" and change:
                    subject = "Odpadá"
                # Searches for the teacher"s shortcut
                index = html.find("bottom", index)
                index = html.find(">", index) + 1
                index = html.find(">", index)
                teacher_to = html.find("<", index)
                teacher = _make_pretty(html[index: teacher_to])
                # Adds the lesson to the timetable
                result[day][i].append(Lesson(name=subject, teacher=teacher,
                    classroom=classroom, theme=theme, change=change, groups=groups))
    return result


def get_timetable(model: Union[SchoolClass, Teacher], timetable_type: TimetableType ) -> List[List[List[Lesson]]]:
    """Returns a timetable for a given class or teacher."""
    return _get_timetable(_get_html(_get_url(timetable_type, model)))
                
 
