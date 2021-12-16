# SAMOGLOSKI = "aeiuy"
# text = "ala ma kot a kto ma ale eeeeee yeye"
# licznik = {}
#
# for znak  in text.lower():
#     if  znak in SAMOGLOSKI:
#         licznik[znak] = licznik.get(znak, 0) +1
#         print(licznik)

waga = 0
produkty = {
    "marchew": 1.23,
    "cebula": 2.30,
    "zeimniaki": 1.34
}
print("Oferta")
for produkt, cena in produkty.items():
    print(f" - {produkt:20} - {cena:3.2f} PLN")

pr = input("co chcesz kupić?")
ile = int(input("Ile? "))
cena = ile * produkt
print("należność", cena)








