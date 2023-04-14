import math

class maize:
    def __init__(self,type,model,price):
        self.price = price
        self.type = type
        self.model = model

    def to_file(self):
        with open(self.model + "txt","w") as f:
            f.write("-Personala datora sastavdala- \nveids: "+self.type+"\nmodelis: "+self.model+"\ncena: "+str(self.price)+" EUR")


part1 = maize('Ram',"corsiar vengeance",99.99)
part1.to_file()