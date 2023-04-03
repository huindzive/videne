class trapece:
    def __init__(self,p1,p2,h):
        self.p1 = p1
        self.p2 = p2
        self.h = h

    def vidus(self):
        return (self.p1 + self.p2) /2

    def laukums(self):
        return self.h * self.vidus()



ss = trapece(6,4,5)
print(ss.laukums())