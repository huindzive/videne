a = []
b = []

x = int(input('ievadi skaitli: '))
while x != 0:
    a.append(x)
    x = int(input('ievadi skaitli: '))


for i in range(len(a)):
    if i % 2 != 0:
        b.append(a[i])

print(b)