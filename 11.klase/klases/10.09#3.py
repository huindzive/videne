class datums:
    def __init__(self,d,m):
        if d < 1 or d>31:
            print('datums neatbilst')
            self.d = 1
        else:
            self.d= d


        if m < 1 or m>12:
            print('datums neatbilst')
            self.m = 1
        else:
            self.m = m

    def printdatums(self):
        return str(self.d) + '/' + str(self.m)

    def next(self):
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
a = datums(30,2)
print('šī diena: ',a.printdatums())
a.next()
print('nākošā diena: ',a.printdatums())