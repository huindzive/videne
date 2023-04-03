# programma, kas no divam katetem aprekina
# taisnlenka trijstura laukumu un perimetru.

import math

a = int(input('ievadi vienu kateti: '))
b = int(input('ievadi otru kateti: '))
c = math.sqrt(a**2+b**2)
p = a + b + c
s = a * b / 2
print('perimetrs: ', p, ' laukums: ', s)
