class Product:
    def __init__(self, id, nazwa, cena):
        self.id= id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f'Product "{self.nazwa}", id:{self.id}, cena: {self.cena} PLN' )

woda = Product( 7, "Woda", 15.22)
#print(woda.nazwa, woda.id, woda.cena)
woda.print_info()