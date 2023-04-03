# 1. Lietotājs vada skaitļus, kamēr ievada 0. Tiek izveidots masīvs no ievadītajiem skaitļiem.

a = []
x = int(input('ievadi skaitli: '))
while x != 0:
    a.append(x)
    x = int(input('ievadi skaitli: '))


# 2. Masīvu izvadīt, izmantojot for ciklu.

for i in range(len(a)):
    print(a[i], end=' ')
print()

# 3. Masīvu izvadīt, izmantojot while ciklu.*

i = 0
while i < len(a):
    print(a[i], end=' ')
    i += 1
print()

# 4. Izvadīt visu elementu summu.

summa = 0
for i in range(len(a)):
    summa += a[i]
print('summa:', summa)

# 5. Masīva elementus ar pāra indeksu izdalīt ar masīva elementiem
# ar nepāra indeksu.*

para = 1
nepara = 1
for i in range(len(a)):
    if (i+1) % 2 == 0:
        para *= a[i]
    else:
        nepara *= a[i]

print(para/nepara)

# 6. Izvadīt masīva lielāko elementu, neizmantojot iebūvētās funkcijas.*
# 7. Izvadīt lielākā elementa pozīciju(indeksu) masīvā.*


lielakais = a[0]
lielakaIndekss = 0
for i in range(1, len(a)):
    if a[i] > lielakais:
        lielakais = a[i]
        lielakaIndekss = i

print('lielakais elements ir', lielakaIndekss + 1, '. elements un tas ir', lielakais)





# 8. Izvadīt masīva mazāko elementu un tā indeksu.

mazakais = a[0]
mazakaIndekss = 0
for i in range(1, len(a)):
    if a[i] < mazakais:
        mazakais = a[i]
        mazakaIndekss = i

print('mazakais elements ir', mazakaIndekss + 1, '. elements un tas ir', mazakais)

# 9. Samainīt masīva lielāko un mazāko elementu vietām.*

# galds = a[lielakaIndekss]
# a[lielakaIndekss] = a[mazakaIndekss]
# a[mazakaIndekss] = galds

a[lielakaIndekss], a[mazakaIndekss] = a[mazakaIndekss], a[lielakaIndekss]
print()
for i in range(len(a)):
    print(a[i], end=' ')
print()


# 10. Atrast biežāk sastopamo elementu, neizmantojot iebūvētās funkcijas.

maxBiezums = 1
biezakaisElements = a[0]
for i in range(len(a)):
    biezums = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            biezums += 1
    if biezums > maxBiezums:
        maxBiezums = biezums
        biezakaisElements = a[i]

print(biezakaisElements, ' sastopams visbiezak - ', maxBiezums, ' reizes')

