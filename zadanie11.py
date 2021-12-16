# x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(x[1])
# print(x[-2])
# print(x[2:7])
# print(x[::3])
# print(x[::-2])
#
# lista = [1,2]
# lista.append(3)
# lista.insert(1,4)
# print(lista)
# lista.pop()
# print(lista)
# lista.extend([4,5,6])
# print(lista)
# lista.index(4,1)
# # lista(range(10))
# # print(lista)
dane = []
i=0
for i in range(10):
    operacja  = input("podaj liczbe lub k by zakończyć:")
    if operacja =="k":
        break
    liczba = int(operacja)
    dane.append(liczba)

print(sum(dane)/ len(dane))

