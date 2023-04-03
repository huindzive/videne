c = []
summa = 0
videjais = 0
vidskaits = 0
x = int(input('ievadi skaitli: '))
c.append(x)
while x != 0:
    x = int(input('ievadi skaitli: '))
    c.append(x)
    if x==0:
        c.remove(0)

if len(c) < 10:
    liels = c[0]
    for i in range(1, len(c)):
        if c[i] > liels:
            liels = c[i]
    print('lielākais: ', liels, 'biežums: ', c.count(liels) )

elif len(c) > 10:
    for i in range(len(c)):
        summa += c[i]
        videjais = summa/len(c)
    for i in range(len(c)):
        print(c[i], end=' ')
    print()
    print('average:',videjais)

    for i in range(len(c)):
        if c[i] < videjais:
            vidskaits += 1

    print(vidskaits)