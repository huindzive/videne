import math
#1. Uzrakstīt funkciju Faktorials(n), kur tiek padots viens arguments - n un funkcija atgriež n faktoriālu.

def faktorials(n):
    if n == 0:
        return 1
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print(faktorials(4))

#2. Uzrakstīt funkciju Diskriminants(a, b, c), kurai padod trīs mainīgos, kas ir koeficienti atbilstoši kvadrātvienādojumam funkcija atgriež diskriminantu.

def diskriminants(a,b,c):
    return (b ** 2) - 4 * a * c

print(diskriminants(4,6,1))

#3
def print_2d(b):
    for i in range(len(b)):
        for j in  range(len(b[i])):
            print(b[i][j], end=' ')