#1. Izveidot masīvu, kas satur skaitļus no 1 līdz 10. Izvadīt masīvu uz ekrāna.

a=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(a)):
    print(a[i], end=' ')
print()

#2. Izveidot masīvu no dažādiem skaitļiem. Izmantojot ciklu un funkciju pop(), dzēst masīva pēdējos 4 elementus.

for i in range(4):
    a.pop()

for i in range(len(a)):
    print(a[i], end=' ')
print()

#3. Izmantojot count() un remove(), dzēst visus pieciniekus no masīva.

b = [1,2,5,2,5,8,5,5,9]

for i in range(b.count(5)):
    b.remove(5)

while b.count(5) > 0:
    b.remove(5)

#4. Lietotājs vada skaitļus, kamēr ievada 0. Tiek izveidots masīvs no ievadītajiem skaitļiem.

c = []
x = int(input('ievadi skaitli: '))
c.append(x)
while x != 0:
    x = int(input('ievadi skaitli: '))
    c.append(x)
    if x==0:
        c.remove(0)

#5. Izvadīt no masīva tos skaitļus, kas lielāki par ievadīto n.
n=int(input('ievadi n: '))
for i in range(len(a)):
    if a[i] > n:
        print(a[i], end=' ')
print()

#6. Izvadīt elementu summu un lielāko elementu, izmantojot ciklus.

summa = 0
for i in range(len(a)):
    summa+= a[i]
print('summa: ',summa)

lielakais = a[0]
for i in range(1, len(a)):
    if a[i] > lielakais:
        lielakais= a[i]

print('leilakais elements: ', lielakais)
#7. Izvadīt pāra skaitļu skaitu masīvā.

pss = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        pss += 1
print(pss)
#8. Programma izvada, kur masīvā atrodas lielākais nepāra skaitlis.

indekss = 0
LNS = 0
for i in range(len(a)):
    if a[i] > LNS and a[i] % 2 != 0:
        LNS = a[i]
        indekss = i
print('lielākais nepāra skaitlis: ' )

#9. Programma izvada tos pāra skaitļus, kuriem ir pāra indekss/pozīcija masīvā.

for i in range(len(a)):
    if i % 2 == 0:
        if a[i] % 2 == 0:
            print(a[i], end="  ")

print()

#10. Ja masīvā ir pāra skaits elementu, izvadīt to no sākuma, citādi izvadīt to no otra gala.

if len(a) % 2 == 0:
    for i in range(len(a)):
        print(a[i], end=' ')
else:
    for i in range(len(a)-1, -1, -1):
        print(a[i], end="  ")
