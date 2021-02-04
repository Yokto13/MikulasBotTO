from adamator import *

tok = get_access_token("https://bakalari.mikulasske.cz/","USERNAME", "PASSWORD")
d = get_marks("https://bakalari.mikulasske.cz/", tok)
for el in d:
    print(el)
    print("-----------------------------------------------")
