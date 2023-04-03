class person:
    def __init__(self,name,surname,height,age):
        self.name = name
        self.surn = surname
        self.height = height
        self.age = age
    
    def fullname(self):
        return self.name + ' ' + self.surn

a = person('Arturs','Balnass',176,17)
print(a.fullname())
