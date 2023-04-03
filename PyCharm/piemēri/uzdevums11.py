import math
a = int(input('ja zinamas abas katetes, ievadi 1\nja zinama katete un laukums, ievadi 2\n'))
if a == 1:
    k1 = int(input('ievadi vienu kateti: '))
    k2 = int(input('ievadi otru kateti: '))
    s = k1 * k2 / 2
    print('laukums ir: ', s)
    hip = math.sqrt(k1 ** 2 + k2 ** 2)
    p = k1 + k2 + hip
    print('perimetrs ir: ', p)
elif a == 2:
    k1 = int(input('ievadi vienu kateti: '))
    s = int(input('ievadi laukumu: '))
    k2 = 2 * s / k1

# ... un ta talak
