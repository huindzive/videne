class prisma:
    def __init__(self,a,b,c,h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def pam_lauk(self):
        s = (self.a + self.b + self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5

    def tilpums(self):
        return self.pam_lauk( ) * self.h

    def sanu_virsma(self):
        return (self.a + self.b + self.c) * self.h

    def pilna_virsma(self):
        return 2*self.pam_lauk() + self.sanu_virsma()

piem = prisma(2,3,4,5)

print('Pamata Laukums: ', piem.pam_lauk())
print('tilpums: ', piem.tilpums())
print('Sānu virsma: ', piem.sanu_virsma())
print('Pilna virsma: ', piem.pilna_virsma())