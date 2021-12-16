tab = [9,7,1,5,3,5,6,22,3,45]


for i in range(len(tab)):
        min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min]:
                min = j
        if i != min:
            print ("\n Krok ", (i+1), ":Wstawianie el min ", tab[min], " na pozycje ", i)
            pom = tab[i]
            tab[i] = tab[min]
            tab[min] = pom
print(tab)