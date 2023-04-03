class person:
    def __init__(self, vards,uzvards,pk):
        self.vards = vards
        self.uzvards = uzvards
        self.pk = pk

    def fullName(self):
        return str(self.vards) + ' ' + str(self.uzvards)


p1 = person('tava','mamma',123456789)

print(p1.fullName())

class teacher(person):
    def priekšmets(self,prieksmets):
        self.priekšmets = prieksmets

    def dati(self):
        print(self.fullName(),self.priekšmets)


class skolens(person):
    def klase(self,klase):
        self.klase = klase

    def setIntereses(self):
        self.intereses = []
        interese = input('ievadi interesi: ')
        while len(interese) > 0:
            self.intereses.append(interese)
            interese = input('ievadi interesi: ')

    def getIntereses(self):
        if self.intereses:
            for interese in self.intereses:
                print(interese)




skolotajs = teacher('Arturs','Balnass','123456-14725')
skolotajs.priekšmets('programmēšana')
skolotajs.dati()
skolenss = skolens('arets','ozols','121212-12457')
skolenss.setIntereses()
skolenss.getIntereses()