# class Osoba:
#     pass
# piotrek = Osoba()
# piotrek.wiek =34
#
# print(piotrek.wiek)

class Osoba:
    gatunek = "Homosapiens"
    def __init__(self, imie, rok_ur,wzrost, waga):
        self.imie = imie
        self.rok_ur = rok_ur
        self.wzrost = wzrost
        self.waga = waga

    def bmi(self):
        return self.waga /(self.wzrost /100) **2

piotrek = Osoba("Piotr", 1986, 181, 82)
print(piotrek.imie, piotrek.waga)

maria = Osoba("Maria",1980,160,65)
print(maria.imie,maria.waga)
print(maria.bmi())
print(Osoba.bmi(piotrek))
print(maria.gatunek)