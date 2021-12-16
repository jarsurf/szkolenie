# cyfry = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print ("    ", end=" ")
# for a in cyfry:
#     print(f"{a:5}", end="")
# print()
# print()
#
# for a in cyfry:
#     print(f"{a}    ",end="")
#     for b in cyfry:
#         print(f"{a * b:5}", end="")
#         print()


cyf = [0, 1, 2, 3, 40, 5, 6, 7, 8, 9]

min = None
max = None
for i, v in enumerate(cyf):
    if v < cyf(min):
        min = i
    if v > cyf(max):
        max = i
    # if min == None or min > i:
    #     min = i
    # if max == None or max < i:
    #     max = i

print("najmniejsza liczba to:", min)
print("największa liczba to:", max)




