pirmais = int(input('ievadi pirmo 3-stura malu'))
otrais = int(input('ievadi otro 3-stura malu'))
tresais = int(input('ievadi treso 3-stura malu'))
pirmais2 = int(input('ievai pirmo 4stura malu'))
otrais2 = int(input('ievadi otru 4stura malu'))
pirmais3 = int(input('ievadi kvadrata malu'))

class triangle:
    def __init__(self, viena, otra, tresa):
        self.viena = viena
        self.otra = otra
        self.tresa = tresa
    
    def darbiba1(self):
        if self.viena+self.otra <= self.tresa or self.viena+self.tresa <= self.otra or self.otra + self.tresa <= self.viena:
            print("trijsturis nesanak")
        else:
            return self.viena+self.otra+self.tresa
        
class taisnsturis:
    def __init__(self, viena, otra):
        self.viena = viena
        self.otra = otra
    def darbiba2(self):
        if self.viena==self.otra:
            print('tas ir kvadrats')
        else:
            return 2*(self.viena+self.otra)
    
class kvadrats:
    def __init__(self, viena):
        self.viena = viena
    def darbiba3(self):
        return 4*self.viena
        
x=triangle(pirmais,otrais,tresais)
y=taisnsturis(pirmais2,otrais2)
z=kvadrats(pirmais3)

print("perimetrs trijstūrim:",x.darbiba1())
print("perimetrs taisnsturim:",y.darbiba2())
print("perimetrs kvadratam:",z.darbiba3())

