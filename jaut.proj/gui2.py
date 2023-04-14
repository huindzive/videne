import sqlite3
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





conn = sqlite3.connect("datasheet.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS datasheet (id INTEGER PRIMARY KEY, type VARCHAR, model VARCHAR, price FLOAT)")

cursor.execute("INSERT INTO datasheet (type,model,price) VALUES (?, ?, ?)", (part1.type,part1.model,part1.price))

cursor.execute("SELECT * FROM datasheet")
records = cursor()
for row in records:
    for value in row:
        

conn.commit()
conn.close()
