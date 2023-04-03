# 1. Lietotājs ievada skaitļus līdz tiek ievadīta 0. Programma izveido masīvu no ievadītajiem skaitļiem.
a = []
x = int(input('ievadi skaitli: '))
a.append(x)
while x != 0:
    x = int(input('ievadi skaitli: '))
    a.append(x)
    if x==0:
        a.remove(0)

# 2. Masīvs tiek izvadīts.
for i in range(len(a)):
    print(a[i], end=' ')

print()

# 3. Programma izvada ievadītā masīva amplitūdu. (lielākā un mazākā elementa starpību)
liels = a[0]
lielsINdeks = 0
for i in range(1, len(a)):
    if a[i] > liels:
        liels= a[i]
        lielsINdeks = i

maz = a[0]
mazIND = 0
for i in range(1,len(a)):
    if a[i] < maz:
        maz = a[i]
        mazIND = i

print('amplitūda:',liels-maz)

# 4. Programma izdzēš no masīva gan lielāko, gan mazāko elementu un izvada jauno masīvu un tā amplitūdu.
a.pop(mazIND) and a.pop(lielsINdeks)

for i in range(len(a)):
    print(a[i], end=' ')

liels2 = a[0]
lielsINdeks2 = 0
for i in range(1, len(a)):
    if a[i] > liels2:
        liels2= a[i]
        lielsINdeks2 = i

maz2 = a[0]
mazIND2 = 0
for i in range(1,len(a)):
    if a[i] < maz2:
        maz2 = a[i]
        mazIND2 = i
print()
print('amplitūda:',liels2-maz2)