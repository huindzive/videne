# 1. Izveidot masīvu a. Pievienot tam divas vērtības – 5 un 12.
a = []
a.append(5)
a.append(12) # [5, 12]
# 2. Masīva sākumā pievienot 5, 3 un 6, taču beigās - 8 un 5.
a.append(8)
a.append(5)
a.insert(0, 5)
a.insert(0, 3)
a.insert(0, 6) # [6, 3, 5, 5, 12, 8, 5]
# 3. Izvadīt masīva trešo elementu.
print(a[2])
# 4. Dzēst masīva trešo elementu. Atkārtoti izvadīt masīva trešo elementu.
a.pop(2)  # [6, 3, 5, 12, 8, 5]

# 5. Izvadīt masīva garumu.
print(len(a))
# 6. Izvadīt vērtības 5 skaitu masīvā.
print(a.count(5))
# 7. Izmantojot ciklu, izvadīt masīvu.
for i in range(len(a)):
    print(a[i], end=' ')
print()
# 8. Izdzēst visus pieciniekus no masīva.
for i in range(a.count(5)):
    a.remove(5)

while a.count(5) > 0:
    a.remove(5)
# 9. Izvadīt masīvu.
for i in range(len(a)):
    print(a[i], end=' ')

# 10. ievadām masīvu b
b = []
for i in range(5):
    x = int(input('ievadi: '))
    b.append(x)

y=int(input('ievadi, kamēr nav nulle: '))
while y!=0:
    b.append(x)
