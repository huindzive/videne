# divdimensiju masiva definesana

a = [[2, 4, 6, 8],
     [1, 3, 5, 7],
     [8, 7, 4, 2],
     [7, 5, 3, 1]]


# patvaliga divdimensiju masiva izvade

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()

# patvaliga x*y izmera masiva izveide + aizpildisana ar 0

c = []
x = 10
y = 10

for j in range(x):
    column = []
    for i in range(y):
        column.append(0)
    c.append(column)


