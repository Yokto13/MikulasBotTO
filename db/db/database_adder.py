"""
Allows for creation of a database or adding answers with keys to an existing one
"""
from .db import DB

def modify_db():
    """ Prompts user to medify a database or create existing one. """
    path = input("Give me path of your db: ")
    is_empty = input("Is your db json empty?y/n ")
    db = None
    if is_empty == 'y':
        db = DB(path, load=False)
    else:
        db = DB(path)
    print("You will be now prompted to fill in the databse.")
    print("You will fill the answer first then the db querries leading to them (questions)")
    print("If you'd like to fill in another set of answers, input 'NEXT'")
    print("If you want to terminate the preocess enter 'END'")
    anss = Answers()
    while (text:=input("Input answer or END: ")) != 'END':
        ans = text
        qs = []
        while (text:=input("Input query or NEXT: ")) != 'NEXT':
            qs.append(text)
        if text == 'NEXT':
            db[ans] = qs
        else:
            anss.add_from_text(text)
    print("Writing the database to the json.")
    db.dumpdb()
    print('DB was saved')
