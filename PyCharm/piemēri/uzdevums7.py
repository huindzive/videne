# lietotajs ievada tris skaitlus, programma izvada
# atbilstosa paralelskaldna tilpumu,
# pilnas virsmas laukumu

a = int(input('ievadi a: '))
b = int(input('ievadi b: '))
c = int(input('ievadi c: '))

v = a * b * c
sv = 2 * (a * b + b * c + a * c)

print('tilpums: ', v, ' virsmas laukums: ', sv)
