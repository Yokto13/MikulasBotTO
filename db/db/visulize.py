from .db import DB

def visulize():
    """ Prints out all keys and coresponding answers in given db. """
    path = input("Path to db json: ")
    db = DB(path)
    for k, v in db.queries_answers():
        print("Key: ",end='')
        print(k)
        print("Answer:")
        print(v)


"""
db['Jak se mas?'].remove_answer_by_text('cooo')
for k, v in db.items():
    print("Key: ",end='')
    print(k)
    print("Answers:")
    v.print_answers()
    
"""
