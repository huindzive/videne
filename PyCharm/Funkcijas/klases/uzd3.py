# klase kvadrātvienādojums
import math
class kvadratvien:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def diskriminants(self):
        return self.b**2 - 4 * self.a * self.c

    def x1(self):
        return (-self.b + math.sqrt(self.diskriminants()))/2 * self.a

    def x2(self):
        return (-self.b - math.sqrt(self.diskriminants())) / 2 * self.a

    def print_roots(self):
        if self.diskriminants() == 0:
            print(self.x1())
        elif self.diskriminants() > 0:
            print(self.x1, ' , ', self.x2)
        else:
            print('sakņu nav')


kvadr1 = kvadratvien(1, -10 , 9)
kvadr1.print_roots()