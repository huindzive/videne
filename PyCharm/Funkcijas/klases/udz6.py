# klase abonoments

class abonoments:
    def __init__(self, menesa_cena):
        self.cena = menesa_cena

    def total_price(self,x):
        return self.cena * x

netflix = abonoments