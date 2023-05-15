import sqlite3

conn = sqlite3.connect("dummj/daasheet.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS persons (id INTEGER PRIMARY KEY, name VARCHAR, surname VARCHAR)")

conn.commit()

name = input('Vārds: ')
surname = input('Uzvārds: ')
cursor.execute("INSERT INTO persons VALUES (?,?)",(name,surname))
conn.commit()

identif = int(input("lalala"))
cursor.execute("DELETE FROM persons WHERE id = ?",str(identif))
conn.commit()
