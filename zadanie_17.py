# def czy_pierwsza(n):
#     if n == 2:
#         return True
#     if n % 2 == 0 or n <= 1:
#         return False
#
# print(czy_pierwsza(6))

def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(czy_pierwsza(3))
print(czy_pierwsza(17))

assert czy_pierwsza(3) is True
