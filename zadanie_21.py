def suma(*args):
    return sum(args)

def mul(*args):
    x =1
    for i in args:
        x*= i
        return x

def dzialania(*args, **kwargs):
    wynik = {}
    for dzialania in kwargs:
        x= kwargs[dzialania](*args)
        wynik[dzialania] = x
        return wynik

print(dzialania(1,2,3,dodawanie=suma))