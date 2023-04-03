#1. Izveidot funkciju, kas pieprasa trīs parametrus – šķautņu garumus. Funkcija atgriež atbilstoša paralēlskaldņa tilpumu.

def skautnes(a,b,c):
    return a * b * c

a = int(input('ievadi 1. šķautni: '))
b = int(input('ievadi 2. šķautni: '))
c = int(input('ievadi 3. šķautni: '))

print('tilpums:',skautnes(a,b,c))
print()

#2. Izveidot funkciju, kas pieprasa trīs parametrus – skaitļa ciparus. Funkcija atgriež atbilstošu trīsciparu skaitli.

def triscipars(a,b,c):
    return (a*100)+ (b*10) + c

a = int(input('ievadi 1. ciparu: '))
b = int(input('ievadi 2. ciparu: '))
c = int(input('ievadi 3. ciparu: '))

print('trīscipars:',triscipars(a,b,c))
print()
#3. Izveidot funkciju, kas pieprasa trīs parametrus – trijstūra. Funkcija atgriež 1, ja trijstūris eksistē, 0, ja trijstūris neeksistē.

def eksistance(a,b,c):
    if a+b > c and a+c > b and b+c >a:
        return 1
    else:
        return 0

a = int(input('ievadi 1. ciparu: '))
b = int(input('ievadi 2. ciparu: '))
c = int(input('ievadi 3. ciparu: '))

print('trijstūra eskistence:',eksistance(0,0,0))