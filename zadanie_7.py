minimum = None
maximum = None
while True:
    polecenie = input("podaj liczbę lub 'k' by zakonczyć")
    if polecenie == "k": break

    if polecenie.isnumeric():
        liczba = int(polecenie)
    else:
        print("podaj liczbę")
    continue

    
    liczba = int(polecenie)
    if minimum is None:
        minimum = liczba
        maksimum = liczba
    else:
        if liczba < minimum:
            minimum = liczba
        if liczba > maksimum:
            maksimum = liczba



