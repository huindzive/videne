# # 1. Uzrakstīt programmu, kas saskaita divus 2x2 masīvus,
# # saskaitot atbilstošos masīvu elementus. Summu glabāt trešajā masīvā.
#
# a = [[1, 4],
#      [7, 3]]
# b = []
# for i in range(2):
#     rin = []
#     for j in range(2):
#         x = int(input('ievadi elementu: '))
#         rin.append(x)
#     b.append(rin)
#
# c = [[0, 0],
#      [0, 0]]
#
# for i in range(2):
#     for j in range(2):
#         c[i][j] = a[i][j] + b[i][j]
#
#
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=" ")
#     print()
# print()
# for i in range(len(b)):
#     for j in range(len(b[i])):
#         print(b[i][j], end=" ")
#     print()
# print()
# for i in range(len(c)):
#     for j in range(len(c[i])):
#         print(c[i][j], end=" ")
#     print()
# print()
#
# # 2. Tas pats ar reizināšanu, veidojot ceturto masīvu.
#
# d = [[0, 0],
#      [0, 0]]
#
# for i in range(2):
#     for j in range(2):
#         d[i][j] = a[i][j] * b[i][j]
#
# for i in range(len(d)):
#     for j in range(len(d[i])):
#         print(d[i][j], end=" ")
#     print()
#
# # 3. Programma, kas rēķina un izvada divdimensiju masīva rindu vidējās vērtības.
#
# for i in range(len(d)):
#     summ = 0
#     for j in range(len(d[i])):
#         summ += d[i][j]
#     print(i + 1, '. rindas summa = ', summ, ' un videja vertiba = ', summ/len(d[i]))

# 4. Programma, kas nxn masīvu aizpilda sekojoši – diagonālē vieninieki, pārējās nulles.

m = []
n = int(input('ievadi n: '))
for i in range(n):
    rin = []
    for j in range(n):
        if i == j:
            rin.append(1)
        else:
            rin.append(0)
    m.append(rin)
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end=" ")
    print()

# Tāds pats masīvs, tikai arī zem diagonāles ir vieninieki.

m = []
n = int(input('Ievadi n: '))
for i in range(n):
    rin = []
    for j in range(n):
        if i == j:
            rin.append(1)
        elif i > j:
            rin.append(1)
        else:
            rin.append(0)
    m.append(rin)
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end=' ')
    print()


