# ievada ievada masīvu, programma pasaka, vai tas ir sakārtots augošā secībā
a = []
x = int(input('ievadi skaitli: '))
a.append(x)
while x != 0:
    x = int(input('ievadi skaitli: '))
    a.append(x)
    if x==0:
        a.remove(0)

for i in range(len(a)):
    print(a[i], end=' ')
print()

indikators = 0
for i in range(len(a)-1):
    if a[i] <= a[i+1]:
        indikators += 1
        break

if indikators == 0:
    print('masīvs ir sakārtots')
else:
    print('masīvs nav sakārtots')
