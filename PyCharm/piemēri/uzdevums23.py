def faktorials(n):
    if n == 0:
        return 1
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def diskriminants(a, b, c):
    return b ** 2 - 4 * a * c


def print_diskriminants(a, b, c):
    print(b ** 2 - 4 * a * c)


def max_2d(a):
    lielakais = a[0][0]
    for i in range(len(a)):
        for f in range(len(a[i])):
            if a[i][f] > lielakais:
                lielakais = a[i][f]
    return lielakais


def print_2d(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()

print(faktorials(4))

print(diskriminants(4, 6, 1))
print_diskriminants(4, 6, 1)

a = []

for j in range(3):
    rin = []
    for i in range(3):
        x = int(input('ievadi masiva elementu: '))
        rin.append(x)
    a.append(rin)

print_2d(a)

print('lielakais elements: ', max_2d(a))
