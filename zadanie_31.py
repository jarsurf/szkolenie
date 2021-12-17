# ith open("dane2.txt", "w") as f:
# dane ="\n".join(lista)

# f.write(dane)

with open("logs.txt", 'w') as file:
   for line in file:
      dane = line.split(';')
      print(dane)
