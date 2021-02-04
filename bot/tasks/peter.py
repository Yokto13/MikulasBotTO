"""
Acts 2:37-38

When the people heard this, they were cut to the heart and
said to Peter and the other apostles, “Brothers, what shall we do?”

Peter replied, “Repent and be baptized, every one of you,
in the name of Jesus Christ for the forgiveness of your sins.
And you will receive the gift of the Holy Spirit.

In this program Saint Peter delivers the gift of the Holy Spirit
in the form of answers to queries to Bakalari.
"""
from .bakalari import keys_of_heaven as KeysOfHeaven

class SaintPeter:
    def __init__(self, user):
        self.user = user

    def handle(self, task: str) -> str:
        """Returns the message for questions about bakalari."""
        if self.user.token is None or not KeysOfHeaven.token_valid(self.user.token):
            if self.user.vip:
                self.user.state = "username"
                return "Zadej, prosím, své uživatelské jméno na Bakaláře."
            else:
                return "Bohužel je kvůli ochraně osobních údajů tato funkce umožněna pouze pro testery."
        print(task)
        if task == "marks":
            marks = KeysOfHeaven.get_marks(self.user.token)
            marks = sorted(marks, key=lambda mark: mark.time_added, reverse=True)
            mark_strings = [mark.to_string() for mark in marks]
            mark_count = len(mark_strings)
            if mark_count == 0:
                return "Za poslední týden nemáš žádné nové známky."
            return f"Za poslední týden máš {mark_count} nových známek:\n" + "\n".join(mark_strings)
        elif task == "message":
            message = KeysOfHeaven.get_message(self.user.token)
            if message is None:
                return "Nemáš žádnou zprávu."
            return "\n".join([
                    "Poslední zprávu ti napsal {message.sender}:",
                    message.title, message.text])
