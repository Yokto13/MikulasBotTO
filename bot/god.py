""" 
A being conceived as the perfect, omnipotent, omniscient
originator and ruler of the universe, the principal object of faith
and worship in monotheistic religions. 
"""
from czert.devil import DevilBot
from user.user import User
from tasks.sinner import Sinner
from tasks.scraper.timetable.models.teachers import Teachers
from tasks.scraper.timetable.models.classes import Classes
import tasks.scraper.news.news_scraper as News

from czert.devil import DevilBot
from user.user import User
import tasks.angel as Angel
import tasks.eve as Eve
import tasks.time_manager as TimeManager
import tasks.bakalari.keys_of_heaven as KeysOfHeaven
from tasks.peter import SaintPeter

class God:
    def __init__(self, db_path = "data/dbtest.json",
            teachers_path = "tasks/scraper/timetable/data/teachers.txt",
            classes_path = "tasks/scraper/timetable/data/classes.csv"):
        self.users = {}
        self.teachers = Teachers(teachers_path)
        self.classes = Classes(classes_path, self.teachers)
        self.devil = DevilBot(db_path, self.teachers, self.classes)
        self.vip_activation_code = "Wh1zzm0tJeNejlepß1!"
        self.vip_deactivation_code = "W1nd0wßJeLepß1NezL1nux!"

    def print_query(self, query: str, token: str) -> None:
        """Prints the answer to the console."""
        print(task)
        print(self._get_answer(query, token))

    def process_query(self, query: str, token: str) -> str:
        """Returns an answer for the given query as a human-readable string.""" 
        # The threshold needs to be adjusted.
        threshold = 3.0
        if token not in self.users:
            self.users[token] = User(token)
        user = self.users[token]
        user.vip = True
        sinner = Sinner(user)
        peter = SaintPeter(user)

        # Handle vip account switching
        if query.strip() == self.vip_activation_code:
            user.vip = True
            return "VIP účet aktivován."
        if query.strip() == self.vip_deactivation_code:
            user.vip = False
            user.token = None
            if user.state != "entity":
                user.state = ""
            user.username = None
            return "VIP účet deaktivován."
        
        # Extract a task from the query.
        task = None
        if user.state == "":
            task = self.devil.answer(query)
            user.last_task = task
        else:
            task = user.last_task
        
        # Handle credentials to Bakalari. 
        if user.state == "username":
            user.username = query.strip()
            user.state = "password"
            return "Poprosím ještě o heslo."
        if user.state == "password":
            user.token = KeysOfHeaven.get_access_token(
                    user.username, query.strip())
            user.username = None
            user.state = ""
            if user.token is None:
                return "Bohužel, uživatelské jméno nebo heslo je chybně."

        # If the entity is wanted, retrieve it from the query.
        entity = None
        if user.state == "entity":
            entity = self.devil.get_closest_entity(query)
        user.entity = ""
        
        # Process task.
        if task is None or task == "":
            return "Bohužel nerozumím tomu, na co se mne ptáš.\nPokud nevíš, co vše umím, můžeš se mne na to zeptat.\nPokud sis jistý, že bych na tvůj dotaz měl znát odpověď, zkus jej přeformulovat."
        elif task[0] == "H":
            return Angel.handle(task[1:], user.vip)
        elif task[0] == "R":
            if entity is None:
                entity = self.devil.get_closest_entity(query)
            if entity == "wrong":
                return "Taková třída u nás na škole není."
            else:
                return sinner.handle(task[1:], entity)
        elif task[0] == "E":
            return Eve.handle(task[1:])
        elif task[0] == "T":
            lesson = self.devil.get_number(query)
            return TaskManager.handle(lesson)
        elif task[0] == "N":
            return News.handle()
        elif task[0] == "B":
            return peter.handle(task[1:])

