# ievada 3 skailtus. programma izvada lielako
# izvadit skaitlus augosa seciba

x = int(input('ievadi pirmo skaitli'))
y = int(input('ievadi otro skaitli'))
z = int(input('ievadi trešo skaitli'))

if x >= y and x >= z:
    if y >= z:
        print(z, y, x)
    else:
        print(y, z, x)
if y >= x and y >= z:
    if x >= z:
        print(z, x, y)
    else:
        print(x, z, y)
if z >= x and z >= y:
    if x >= y:
        print(y, x, z)
    else:
        print(x, y, z)



