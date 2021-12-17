# f = open("dane.txt", "w")
# f.write("Ala   \n")
# f.write("Kottttttttt")
# f.close()

# with open("dane.txt") as f:
#     for line in f:
#         print(line)


# with open(,"w") as f:
#     f.write()

lista = ["XXX", "YYY", "ZZZ"]
#
# plik = open("dane2.txt", 'w')
# plik.writelines(lista)
# plik.close()

with open("dane2.txt", "w") as f:
   dane ="\n".join(lista)
   f.write(dane)




