# lista = [1,23,4,5,7,6]
# for i in range(len(lista)):
#     dopisz = True
#     for j in range(i):
#       if (lista[i] == lista[j]):
#         dopisz = False
#         break
#     if (dopisz):
# #       wynik.append(lista[i])
# # return wynik

lista = [1, 23, 4, 5, 7, 6]
    for i in range(len(lista)):
        dopisz = True
        for j in range(i):
            if (lista[i] == lista[j]):
                dopisz = False
                break




print("Podaj elementy tablicy:")
lista = [int(x) for x in input().split()]
print("Unikalne elementy to:")
wynik = unikalneElementy(lista)
for x in wynik:
    print(x, end=' ')