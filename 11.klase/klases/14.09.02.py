class sekmjuizraksts:
    def __init__(self):
        self.sekmes = []
    
    def atzime(self,a):
        if 1<=a and a<=10:
            self.sekmes.append(a)
    
    def videjais(self):
        return sum(self.sekmes)/len(self.sekmes)

pd = sekmjuizraksts()
pd.atzime(5)
pd.atzime(7)
print(pd.videjais())
