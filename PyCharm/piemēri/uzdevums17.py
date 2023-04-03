# 1. Lietotājs vada skaitļus, kamēr ievada 0.
# Tiek izveidots masīvs no ievadītajiem skaitļiem sekojoši
# – nepāra skaitļi sākumā, pāra – beigās.

a = []

x = int(input('ievadi skaitli: '))
while x != 0:
    if x % 2 == 0:
        a.append(x)
    else:
        a.insert(0, x)
    x = int(input('ievadi skaitli: '))


for i in range(len(a)):
    print(a[i], end='')
print()

# 2. Izvadīt no masīva tos skaitļus, kas lielāki par ievadīto n.

n = int(input('ievadi n: '))
print('skaitli masiva, kas lielaki par n: ', end=' ')

for i in range(len(a)):
    if a[i] > n:
        print(a[i], end=' ')
print()

# 3. Lietotājs vada skaitļus, kamēr ievada 0.
# Tiek izveidots masīvs no ievadītajiem skaitļiem.

b = []

x = int(input('ievadi skaitli: '))
while x != 0:
    b.append(x)
    x = int(input('ievadi skaitli: '))

# 4. Tiek izvadīts katrs otrais masīva elements, ja tas ir pāra skaitlis.

for i in range(len(b)):
    if (i+1) % 2 == 0:
        if b[i] % 2 == 0:
            print(b[i], end=' ')
print()
