
def wypisz(tab):  # tworzymy metode do wypiswania zawartosci naszej tablicy
    for el in tab:
        print(el, end=" | ")


def sortuj_wybor(tab, n):
    for x in range(n - 1):  # iterujemy poprzez wszsytkei elementy tablicy, poza ostatnim
        minimum = x  # usatwiamy aktualny element jako ten najmniejszy
        for j in range(x + 1, n):  # a nastepnie szukamy elementow od niego mniejszych
            if tab[j] < tab[minimum]:
                minimum = j
        if x != minimum:  # jezeli znajdziemy element jakkolwiek mniejszy
            print("\nKrok ", (x + 1), ": wstawianie elementu minimalnego ", tab[minimum], " na pozycje ", x)
            pom = tab[x]  # dokonujemy jego zamiany
            tab[x] = tab[minimum]
            tab[minimum] = pom


print("Podaj ilosc elementow tablicy:")
a = int(input())
tablica = []
for i in range(a):
    print("Podaj element nr. ", (i + 1))
    tablica.append(int(input()))
print("Oto twoja tablica:")
wypisz(tablica)
sortuj_wybor(tablica, a)
print("Oto twoja tablica po sortowaniu:")
wypisz(tablica)