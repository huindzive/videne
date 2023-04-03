# Klase Kvadratvienadojums
import math


class Kvadratvienadojums:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def diskrimants(self):
        return self.b ** 2 - 4 * self.a * self.c

    def x1(self):
        return (-self.b + math.sqrt(self.diskrimants()))/2 * self.a

    def x2(self):
        return (-self.b - math.sqrt(self.diskrimants()))/2 * self.a

    def print_roots(self):
        if self.diskrimants() == 0:
            print(self.x1())
        elif self.diskrimants() > 0:
            print(self.x1(), ', ', self.x2())
        else:
            print('saknu nav')


kvadrvien1 = Kvadratvienadojums(1, -10, 9)
kvadrvien1.print_roots()
