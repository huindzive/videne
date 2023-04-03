a = []
velamais_izmers = 5

for i in range(velamais_izmers):
    x = int(input("ievadi masiva " + str(i+1) + ". elementu ")) # str parveido skaitlisku vertibu par vienkarsu tekstu
    a.append(x) # append pievieno masiva gala elementu


for i in range(len(a)): # sads cikls izdruka patvaliga izmera masivu, jo funkcija len pasaka,
    print(a[i], end=" ") # cik gars ir masivs, tadejadi ari cik gars bus cikls

for i in range(len(a)): # katram masiva elementam pieskaitam 5
    a[i] += 5

print()

for i in range(len(a)): # atkal izdrukajam
    print(a[i], end=" ")

a.pop() # neko neievadot iekavas, no masiva beigam tiek dzests viens elements
a.pop(2) # vertiba iekavas norada masiva elementa indeksu, kurs tiks izdzests

# ieprieksejas divas rindinas izdzesa pedejo un treso masiva elementu

print()

for i in range(len(a)): # atkal izdrukajam
    print(a[i], end=" ")

a.remove(6) # remove funkcija mekle elementa vertibu, nevis indeksu, sanak no masiva dzesisim sesinieku
a.count(1) # saskaita vieninieku skaitu masiva
a.insert(0, 6) # masiva 0taja pozicija ievietojam 6
b = [1, 2, 3]
a.extend(b) # papildinam masivu a ar b masiva vertibam 