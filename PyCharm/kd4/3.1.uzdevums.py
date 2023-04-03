a = []

for j in range(3):
    rinda = []
    for i in range(3):
        x = int(input('ievadi masīva elementu: '))
        rinda.append(x)
    a.append(rinda)

lielakais = a[0][0]
x=0
y=0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] > lielakais:
            lielakais = a[i][j]
            x = i
            y = j
print('lielākais elements', lielakais, ' artodas:(', x+1,',',y+1,')')

sum = 0
for i in range(3):
    sum += a[i][i]

print('diagonāles summa: ',sum)