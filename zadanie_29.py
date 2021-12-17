class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return(self.x + other.x, self.y + other.y)

v1 = Vector(1,1)
v2 =Vector(2,2)
assert  v1+ v2 == Vector(3,3)
    # def dodanie_wektora(self):
