# Programma izvada, kurš ir lielāks - masīva pirmais vai pēdējais elements.

a = [1, 2, 3, 1, 0, 5]
print(a)
if a[0] >= a[-1]:
    print('pirmais lielaks par pedejo')
else:
    print('pedejais  lielaks  par pirmo')

# Lietotājs ievada skaitļus līdz tiek ievadīta nulle.
# Tie tiek pievienoti masīvam, ja ir lielāki par iepriekš
# ievadīto.
# 1 2 2 1 4 2 0      a = [1, 2, 4]

a = []
x = int(input('ievadi skaitli: '))
a.append(x)
while x != 0:
    x = int(input('ievadi skaitli: '))
    if x > a[-1]:
        a.append(x)

# Masīvu izvada no sākuma, kā arī no beigām.

for i in range(len(a)):
    print(a[i], end=' ')

print()

for i in range(len(a)-1, -1, -1):
    print(a[i], end=' ')
