class Taisnturis:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def p(self):
        return 2*(self.a + self.b)

    def s(self):
        return self.a * self.b


import math


class Cilindrs:
    def __init__(self, radiuss, h):
        self.r = radiuss
        self.h = h

    def pamata_s(self):
        return math.pi * pow(self.r, 2)

    def v(self):
        return self.pamata_s() * self.h

    def surface(self):
        return 2 * math.pi * self.r + 2 * self.pamata_s()


class Paralelskaldnis:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def v(self):
        return self.a * self.b * self.c

    def sanu_virsma(self):
        return 2 * (self.a * self.b + self.a * self.c + self.c * self.b)


a = Paralelskaldnis(1, 2, 3)

x = Taisnturis(5, 7)
print(x.a)
print(x.s(), ' ', x.p())

y = Cilindrs(6, 12)
print(round(y.surface(), 2))
print(y.r)

