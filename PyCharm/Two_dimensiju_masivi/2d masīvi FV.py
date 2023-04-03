#1. Lietotājs ievada 3x3 masīva elementus. Programma izvada masīvu, tā lielāko elementu un visu elementu summu.

b = []
for i in range(3):
    rin = []
    for j in range(3):
        x=int(input('ievadi elementu: '))
        rin.append(x)
    b.append(rin)

for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=' ')
    print()
print()

sum = 0
for i in range(len(b)):
    for j in range(len(b[i])):
        sum+=b[i][j]
print('summa: ', sum)

lielakais = b[0][0]
for i in range(len(b)):
    for j in range(len(b[i])):
        if b[i][j] > lielakais:
            lielakais = b[i][j]
print('lielākais elements', lielakais)

#2. Izvadīt tos elementus, kas neatrodas uz diagonāles.

for i in range(3):
    for j in range(3):
        if i != j:
            print(b[i][j], end=' ')
print()

#3. Izvadīt masīva otro rindu un pirmo kolonu.

for j in range(len(b[1])):
    print(b[1][j], end=' ')
print()
print()
for i in range(len(b)):
    print(b[i][0])

print()

#4. Lietotājs ievada skaitli, programma izvada šī skaitļa atrašanos vietu masīvā. Piemēram, lietotājs ievada 5, programma pasaka, ka šis skaitlis atrodas 2. rindas 1. kolonnā.

x=0
y=0
liet=int(input('ievadi skaitli kuru meklē: '))
for i in range(3):
    for j in range(3):
        if liet == b[i][j]:
            x += i
            y += j
            print('skaitlis: ',liet, 'atrodas ',x+1, '. rindā, ',y+1,'. kolonnā')