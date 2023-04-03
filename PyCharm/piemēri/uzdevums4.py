# lietotajs ievada skaitli. programma izvada si skaitla faktorialu.

x = int(input('ievadiet skaitli: '))

faktorials = 1

# for i in range(1, x + 1):
#     faktorials *= i

i = 1

while i <= x:
    faktorials *= i
    i += 1

print(faktorials)
