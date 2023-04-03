import math
class cilindrs:
    def __init__(self, radiuss, h):
        self.h = h
        self.r = radiuss

    def pamat_s(self):
        return math.pi * pow(self.r, 2)

    def v(self):
        return self.pamat_s() * self.h

    def surface(self):
        return 2 * math.pi * self.r + 2 * self.pamat_s()

x = cilindrs(6, 12)
print(x.surface)



class paralelograms:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def v(self):
        return self.a * self.b * self.c

    def sanu_virsma(self):
        return 2*(self.a * self.b + self.c * self.b + self.a * self.c)

a = paralelograms(1,2,3)
print(a.sanu_virsma())