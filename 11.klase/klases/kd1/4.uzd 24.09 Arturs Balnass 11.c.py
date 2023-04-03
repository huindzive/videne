class stunda:
    def __init__(self,h):
        self.h = h
    def add(self,ad):
        self.h += ad
        while self.h > 23:
            self.h -= 24

        return self.h


ss = stunda(23)
print(ss.add(60))