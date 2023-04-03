# klase Abonements

class Abonements:
    def __init__(self, menesa_cena):
        self.cena = menesa_cena

    def total_price(self, x):
        return self.cena * x


netflix = Abonements(10.99)
print(netflix.total_price(12))
