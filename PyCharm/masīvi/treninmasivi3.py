# 1. Lietotājs vada skaitļus, kamēr ievada 0. Tiek izveidots masīvs noievadītajiem skaitļiem sekojoši –nepāra skaitļi sākumā, pāra –beigās.

a = []
x = int(input('ievadi skaitli: '))
#while x != 0:
 #   x = int(input('ievadi skaitli: '))
  #  a.append(x)
   # if x==0:
    #    a.remove(0)


while x != 0:
    if x % 2 == 0:
        a.append(0,x)
    else:
        a.insert(0, x)
    x = int(input('ievadi skaitli: '))

# 2. izvadīt no masīva tos skaitļus kas lielāki par ievadīto 'N'

n = int(input('ievadi n:'))
print('skaitli masīva, kas lielāki par n:', end=' ')
for i in range(len(a)):
    if a[i] > n:
        print(a[i], end=' ')
print()

# 3. lietotājs vada skaitļus, kamēr ievada 0. tiek izveidots masīvs no ievadītajiem skaitļiem

b = []

x = int(input('ievadi skaitli: '))
b.append(x)
while x != 0:
    x = int(input('ievadi skaitli: '))
    b.append(x)
    if x==0:
        a.remove(0)

# 4. tiek izvadīts katrs otrais masīva elements, ja tas ir pāra skaitlis.

for i in range(1,len(b), 2):
    if b[i] % 2 == 0:
        print(b[i], end=' ')
print()