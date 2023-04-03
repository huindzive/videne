# 1. Izveidot masīvu a. pievienot tam divas vērtības - 5 un 12
a = []
a.append(5)
a.append(12)

# 2. Masīva sākumā pievienot 5, 3 un 6, taču beigās - 8 un 5
a.append(8)
a.append(5)
a.insert(0,5)
a.insert(0,3)
a.insert(0,6)

# 3. Izvadīt masīva trešo elementu
print(a[2])

# 4. Dzēst masīva trešo elementu. atkārtoti izvadīt masīva trešo elementu
a.pop(2)

# 5. Izvadīt masīva garumu.
print(len(a))

# 6. Izvadīt vērtības 5 skaitu
print(a.count(5))

# 7. Izmantojot ciklu, izvadīt masīvu
for i in range(len(a)):
    print(a[i], end=' ')

print()

# 8. izdzēst visus pieciniekus no masīva
for i in range(a.count(5)):
    a.remove(5)

while a.count(5) > 0:
    a.remove(5)

# 9. izvadīt masīvu
for i in range(len(a)):
    print(a[i], end= ' ')







































