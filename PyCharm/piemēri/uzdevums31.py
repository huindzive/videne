# Klase Date un iekšējā funkcija tomorrow()


class Date:
    def __init__(self, day, month):
        self.d = day
        self.m = month

    def tomorrow(self):
        if self.m == 2:
            if self.d == 28:
                self.m += 1
                self.d = 1
            else:
                self.d += 1
        elif self.m == 4 or self.m == 6 or self.m == 9 or self.m == 11:
            if self.d == 30:
                self.m += 1
                self.d = 1
            else:
                self.d += 1
        else:
            if self.d == 31:
                if self.m == 12:
                    self.d = 1
                    self.m = 1
                else:
                    self.m += 1
                    self.d = 1
            else:
                self.d += 1

    def print(self):
        print(self.d, '/', self.m)

    def yesterday(self):
        for i in range(364):
            self.tomorrow()


d = Date(31, 3)
d.print()
d.yesterday()
d.print()


















