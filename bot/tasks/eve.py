"""
The woman stared at the fruit. 
It looked beautiful and tasty. 
She wanted the wisdom that it would give her, and she ate some of the fruit. 
Her husband was there with her, so she gave some to him, and he ate it too.
Genesis 3:6

As Eve gave her beloved husband food so does this piece of code.
Or at least it says what the man will eat this day according to the
Ejidelnicek...
"""
import requests
import re
from typing import Dict, Union, List
from datetime import date

ejidelnicek_url ="http://php2.e-jidelnicek.cz/menu/?canteenNumber=11160"
ejidelnicek_url ="http://php2.e-jidelnicek.cz/menu/?canteenNumber=11160&from_date=2020-12-02"


def _get_html(url: str) -> str:
    " Returns html code of the given url. "
    r = requests.get(url)
    return r.text


def _get_days(html: str) -> str:
    pattern = '<h2 class="menu-day">(.*)<\/h2>'
    return re.findall(pattern, html)


def _get_meals_by_day(html: str, day: str) -> Dict[str, Union[str, List[str]]]:
    """ Given a day that is written in the html returns meals
    corresponding to it. """
    # Get the beggining.
    meals_html = html.split(day)[1] 
    # Get end.
    meals_html = meals_html.split('<div class="canteen-menu">')[0]
    pattern = '<dd class="menu-name"><h4>(.*)<\/h4><\/dd>'
    meals = re.findall(pattern, meals_html)
    if meals is not None and len(meals):
        d_meals = {}
        d_meals['soup'] = meals[0]
        d_meals['main dishes'] = meals[1:]
        return d_meals
    return None


def _get_current_date():
    """ Gets current date in readable format used by ejidelnicek. 

        The format id DD. MM.
    """
    # today = date.today()
    today = date(2020, 12, 3)
    return f"{today.day}. {today.month}."


def _get_todays_meals() -> str:
    """ Returns string to be printed to the user. """
    html = _get_html(ejidelnicek_url)
    day = _get_current_date()
    d_meals = _get_meals_by_day(html, day)
    if d_meals is not None:
        message = f""" 
            V jídelně na CG je dnes k obědu:
            Polévka: {d_meals['soup']}
            Hlavní chody: 
        """
        for meal in d_meals['main dishes']:
            message += f"{meal}\n"
        return message
    else:
        return "Jídelna na dnešek jídla nenabízí."


def handle(task: str) -> str:
    return _get_todays_meals()


"""
# Should be probably moved to tests.
html =  _get_html(ejidelnicek_url)
print(_get_days(html))
for day in _get_days(html):
    print(day)
    print(_get_meals_by_day(html, day))

print(get_todays_meals())
"""
