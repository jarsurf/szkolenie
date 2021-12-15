pozycja_x = int(input("Pozycja Gracza X: "))
pozycja_y = int(input("Pozycja Gracza Y: "))


if pozycja_x < 10:
    if pozycja_y < 10:
        print("Gracz jest w DL")
    elif pozycja_y >= 10 and pozycja_y > 90:
        print("Gracz jest w L")
    elif pozycja_y > 90:
        print("Gracz jest w GL")
if pozycja_x > 10 and pozycja_x < 90:
    if pozycja_y < 10:
        print("Gracz jest w D")
    elif pozycja_y >= 10 and pozycja_y > 90:
        print("Gracz jest w C")
    elif pozycja_y > 90:
        print("Gracz jest w G")
if pozycja_x < 90:
    if pozycja_y < 10:
        print("Gracz jest w DP")
    elif pozycja_y >= 10 and pozycja_y > 90:
            print("Gracz jest w P")
    elif pozycja_y > 90:
            print("Gracz jest w GP")


