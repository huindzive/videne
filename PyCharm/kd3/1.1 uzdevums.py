c = []
x = int(input('ievadi skaitli: '))
c.append(x)
while x != 0:
    x = int(input('ievadi skaitli: '))
    c.append(x)
    if x==0:
        c.remove(0)

for i in range(len(c)):
    if c[i] % 2 == 0:
        print(c[i], end=" ")