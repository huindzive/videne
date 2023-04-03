#1
a = []
for i in range(3):
    rind = []
    for f in range(3):
        x = int(input("ievadi skaitli"))
        rind.append(x)
    a.append(rind)

sum = 0
for i in range(len(a)):
    for f in range(len(a[i])):
        sum += a[i][f]
print("summa ir", sum)

lielakais = a[0][0]
for i in range(len(a)):
    for f in range(len(a[i])):
        if a[i][f] > lielakais:
            lielakais = a[i][f]
print("lielakais ir", lielakais)

#2
for i in range(3):
    for f in range(3):
        if i != f:
            print(a[i][f])

#3
for i in range(len(a[1])):
    print(a[1][i])
print()
for i in range(len(a)):
    print(a[i][0])

#4
x = 0
y = 0
skaitlis = int(input("ievadi skaitli"))
for i in range(3):
    for f in range(3):
        if skaitlis == a[i][f]:
            x = i
            y = f
            print("Skaitlis atrodas", x, ". rindas", y, ". kolonnā.")
