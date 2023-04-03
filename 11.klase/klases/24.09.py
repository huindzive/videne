import math
class paralelskaldnis:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def virsma(self):
        return 2 * (self.a * self.b) + 2 * (self.a * self.c) + 2 * (self.c * self.b)

    def tilpums(self):
        return self.a * self.b * self.c

    def diagonale(self):
        d = math.sqrt(self.a ** 2 + self.b ** 2)
        return math.sqrt(self.c ** 2 + d ** 2)

kkas = paralelskaldnis(3,4,6)
print('Pilna virsma: ',kkas.virsma())
print('Tilpums: ',kkas.tilpums())
print('Diagonāle: ',kkas.diagonale())