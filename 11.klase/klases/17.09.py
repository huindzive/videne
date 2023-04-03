class kvadratvien:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def diskriminants(self):
        return self.b**2 - 4 * self.a * self.c

    def sakne1(self):
        if self.diskriminants() >=0:
            return (-self.b + self.diskriminants()**0.5)/(self.a * 2)

    def sakne2(self):
        if self.diskriminants() >=0:
            return (-self.b - self.diskriminants()**0.5)/(self.a * 2)

    def xvirsotne(self):
        return -self.b / (2*self.a)

    def yvirsotne(self):
        return self.a * self.xvirsotne()**2 + self.b * self.xvirsotne() +  self.c * self.xvirsotne()

vien = kvadratvien(4 , 6 , 2)
print('D = ',vien.diskriminants())
print('x1 = ', vien.sakne1())
print('x2 = ', vien.sakne2())
print('parabolas virsotne = (',vien.xvirsotne(), ',', vien.yvirsotne(),')')