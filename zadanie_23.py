def formatuj(*args,**kwargs):
    print(args)
    print(kwargs)
    napis= ""
    for n in args:
        napis += "\n" + n
    for klucz, text in kwargs.items():
        napis = napis.replace('$' + klucz, str(text))
        return napis

formatuj(
    'koszt $cena PLN',
    'kwot $cena brutto. Pdatek $podatek %',
    cena=10,
    podatek=23
)
print