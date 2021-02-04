"""
    A spiritual being superior to humans in power and intelligence.

    Came to this program to guide users on their quest.
"""

def handle(task: str, vip: bool) -> str:
    """Returns predifen answers to common general questions."""
    if task == "ahoj":
        return "Ahoj! Co pro tebe můžu udělat?"
    elif task == "ahojb":
        return "Ahoj člověče :D"
    elif task == "help":
        return "Přemýšlíš-li, co umím, tady je seznam věcí, se kterými ti dokáži pomoci:\n - Zjistit, jakou máš hodinu, denní rozvrh, do jaké třídy máš jít.\n - Podívat se, co bude dnes k obědu.\n - Přečíst zprávy ze stránek školy."
    elif task == "whizzmot":
        return "Jsi skvělý, můj uživateli. Ale na světě i v zemi zdejši, Whizzmot je nejskvělejši."
    elif task == "reditel":
        return "Petr Mazanec je ředitel."
    elif task == "poradce":
        return "Ivana Šafránková je výchovný poradce."
    elif task == "spravce":
        return "Pepa Červenec je správce sítě."
    elif task == "adresa":
        return "Mikulášské nám. 23, Plzeň, 326 00."
    elif task == "email":
        return "Kontaktní email je kontakt@mikulasske.cz."
    elif task == "phone":
        return "Kontaktní telefon je 377 226 564."
    elif task == "ico":
        return "IČO je 49778145."
    elif task == "otevirani":
        return "Škola je otevřená v pracovní dny od 6:30 do 18:30."
    elif task == "vesmir":
        return "41.9999998 (omluv mé zaokrouhlovací chyby)"
    elif task == "nalada":
        return "Mám se dobře. Doufám že ty rovněž :D"
    elif task == "diky":
        return "Není zač :D"  
    elif task == "nic":
        return "👍"  
    elif task == "stone":
        if vip:
            return "🪨"
        else:
            return "Bohužel nemáš vipko."
    else:
        raise ValueError(f"Identifier {task} is invlaid.")


