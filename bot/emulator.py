print("Importing...")
from god import God
print("All imports were sucessuful.")
print("Instantiating god...")
g = God()
print("")
print("God was created successfuly.")
print("You can now talk to Mikulas.")
print("When you get bored just type 'END' to close this program")
while (text:=input()) != "END":
    print("Asking Mikulas about:")
    print(text)
    print(g.process_query(text, "tok"))

