#kilo = 10
#print("Cena za kg: ", kilo)
#waga = input("Waga: ")
#waga = float(waga)
#naleznosc = kilo * waga
#print("Naleznosc: ", naleznosc)



# nazwa_1 = "Cheddar"
# cenna_1 = 100
#
# nazwa_2 = "Gouda"
# cenna_2 = 12.456
#
# template = "Ser: {:10} - cena {:6.2f}"
# print(template.format(nazwa_1, cenna_1))
# print(template.format(nazwa_2, cenna_2))

miasto_a = input("Miasto A: ")
miasto_b = input("Miasto B: ")
dystans = int(input(f"Podaj dystans: {miasto_a}-{miasto_b} "))
paliwo = float(input("Cena paliwa: "))
spalanie_deklarowane = float(input("Podaj spalnaie na 100km: "))
koszt = round(dystans/100 * spalanie_deklarowane * paliwo)
print(f"Koszt przejazdu na trasie {miasto_a}-{miasto_b} to {koszt} PLN")
