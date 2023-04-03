# 1. Uzrakstīt programmu, kas ļauj ievadīt lietotājam 3x3 masīva elementus.

a = []

for j in range(3):
    rin = []
    for i in range(3):
        x = int(input('ievadi masiva elementu: '))
        rin.append(x)
    a.append(rin)

# 2. Izvada ievadīto masīvu, izmantojot ciklu ciklā.

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
print()

# 3. Izvada otro rindu no masīva. Izvada trešo kolonnu.
# (rindas iet horizontāli, kolonnas – vertikāli.

for j in range(len(a[1])):
    print(a[1][j], end=' ')
print()
print()
for i in range(len(a)):
    print(a[i][2])

# 4. Programma izvada 3x3 masīva elementu summu.

sum = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        sum += a[i][j]
print('summa: ', sum)

# 5. Programma izvada masīva lielāko elementu.

lielakais = a[0][0]
x = 0
y = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] > lielakais:
            lielakais = a[i][j]
            x = i
            y = j
print('lielakais elements ', lielakais, ' atrodas:(', x + 1, ',', y + 1, ')')

# 6. Programma izvada summu katrai masīva rindai(1. rindas elementu summa
# ir …, 2. rindas.. utt.)

for i in range(len(a)):
    summ = 0
    for j in range(len(a[i])):
        summ += a[i][j]
    print(i + 1, '. rindas summa = ', summ)

# 7. Nosaka, kuras rindas elementu summa ir lielākā.

lielsum = 0
rinr = 0
for i in range(len(a)):
    summ = 0
    for j in range(len(a[i])):
        summ += a[i][j]
    if summ > lielsum:
        lielsum = summ
        rinr = i
print('lielaka summa ir ', rinr + 1, '. rindai un ta ir ', lielsum)
