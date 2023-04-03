# 1. Izveidot masīvu, kas satur skaitļus no 1 līdz 10. Izvadīt masīvu uz ekrāna.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(1, 11):
#     a.append(i)

print(a)
for i in range(len(a)):
    print(a[i], end=' ')
print()

# 2. Izveidot masīvu no dažādiem skaitļiem. Izmantojot ciklu un funkciju pop(), dzēst masīva pēdējos 4 elementus.

for i in range(4):
    a.pop()

for i in range(len(a)):
    print(a[i], end=' ')
print()

# 3. Izmantojot count() un remove(), dzēst visus pieciniekus no masīva.

b = [1, 2, 5, 2, 5, 8, 5, 5, 9]

for i in range(b.count(5)):
    b.remove(5)

for i in range(len(b)):
    print(b[i], end=' ')
print()


# 4. Lietotājs vada skaitļus, kamēr ievada 0. Tiek izveidots masīvs no ievadītajiem skaitļiem.

a = []

x = int(input('ievadi skaitli: '))
while x != 0:
    a.append(x)
    x = int(input('ievadi skaitli: '))

print('masivs: ')
for i in range(len(a)):
    print(a[i])

print()

# 5. Izvadīt no masīva tos skaitļus, kas lielāki par ievadīto n.

n = int(input('ievadi n: '))
for i in range(len(a)):
    if a[i] > n:
        print(a[i], end=' ')
print()

# 6. Izvadīt elementu summu un lielāko elementu, izmantojot ciklus.

for i in range(len(a)):
    print(a[i], end=' ')
print()
summa = 0
lielakais = a[0]
for i in range(len(a)):
    summa += a[i]
    if a[i] > lielakais:
        lielakais = a[i]

print('summa: ', summa)
print('lielakais: ', lielakais)


# 7. Izvadīt pāra skaitļu skaitu masīvā.

paraSkaitluSkaits = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        paraSkaitluSkaits += 1

print('masiva ir ', paraSkaitluSkaits, ' para skaitli')

# 8. Programma izvada, kur masīvā atrodas lielākais nepāra skaitlis.

indekss = 0
lielakaisNepara = 0
for i in range(len(a)):
    if a[i] > lielakaisNepara and a[i] % 2 != 0:
        lielakaisNepara = a[i]
        indekss = i

print('lielakais nepara skaitlis atrodas ', indekss, '. pozicija')


# 9. Programma izvada tos pāra skaitļus, kuriem ir pāra indekss/pozīcija masīvā.

for i in range(len(a)):
    if i % 2 == 0:
        if a[i] % 2 == 0:
            print(a[i], end=' ')


print()

# 10. Ja masīvā ir pāra skaits elementu, izvadīt to no sākuma, citādi izvadīt
#     to no otra gala.

if len(a) % 2 == 0:
    for i in range(len(a)):
        print(a[i], end=' ')
else:
    for i in range(len(a)-1, -1, -1):
        print(a[i], end=' ')
