#1 Lietotājs vada skaitļus, kamēr ievada 0. Tiek izveidots masīvs no ievadītajiem skaitļiem

a = []
y=0
x = int(input('ievadi skaitli: '))
a.append(x)
while x != 0:
    x = int(input('ievadi skaitli: '))
    a.append(x)
    if x==0:
        a.remove(0)

#2 Masīvu izvadīt izmantojot for ciklu

for i in range(len(a)):
    print(a[i], end=' ')

print()

#3 masīvu izvadīt izmantojot while ciklu

while y != 1:
    y+=1
    print(a)

print()

while y < len(a):
    print(a[y], end='')
    y += 1

print()

#4 izvadīt visu elementu summu

summa = 0
for i in range(len(a)):
    summa+= a[i]
print('summa:', summa)

#5 Masīva elementus ar pāra indeksu izdalīt ar masīva elementiem ar nepāra indeksu

para = 1
nepara = 1
for i in range(len(a)):
    if (i+1) % 2 == 0:
        para *= a[i]
    else:
        nepara *= a[i]
print(para/nepara)

#6 Izvadīt masīva lielāko elementu, neizmantojot iebūvētās funkcijas
#7 Izvadīt lielākā elementa pozīciju(indeksu) masīvā

lielakais = a[0]
lielakaIndekss = 0
for i in range(1, len(a)):
    if a[i] > lielakais:
        lielakais= a[i]
        lielakaIndekss = i

print('leilakais elements: ', lielakais)
print(lielakaIndekss +1,'elements un tas ir', lielakais)


#8 izvadīt masīva mazāko elementu un tā indeksu

mazakais = a[0]
mazakaindekss
for i in range(1,len(a)):
    if a[i] < mazakais:
        mazakais = a[i]
        mazakaindekss = i

print('mazakais elements: ', mazakais)
print(mazakaindekss +1,'elements un tas ir', mazakais)

#9 samainīt masīva lielāko un mazāko elementu vietām
a[lielakaIndekss], a[mazakaindekss] = a[mazakaindekss], a[lielakaIndekss]

galds = [lielakaIndekss]
a[lielakaIndekss] = a[mazakaindekss]
a[mazakaindekss] = galds
for i in range(len(a)):
    print(a[i], end=' ')
print()


#10 Atrast biežāk sastopamo elementu, neizmantojot iebūvētās funkcijas
maxBiezums = 1
for i in range(len(a)):
    biezums = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            biezums += 1







