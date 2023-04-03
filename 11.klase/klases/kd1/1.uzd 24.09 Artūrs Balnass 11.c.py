import math
class TaisnlenkaTristuris:
    def __init__(self,k1,k2):
        self.k1 = k1
        self.k2 = k2

    def perimetrs(self):
        d = math.sqrt(self.k1 **2+self.k2**2)
        return self.k1 + self.k2 + d

    def laukums(self):
        return (self.k1 * self.k2)/2