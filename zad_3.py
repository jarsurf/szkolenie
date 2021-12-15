import datetime

rok_urodzenia = int(input("Podaj rok urodzenia: "))
cur_date= datetime.datetime.now
rok = 2021
if rok - rok_urodzenia <= 18:
    print("Jestes niepelnoletni!")
else:
    print("Jestes pelnoletni!")
