# lietotajs ievada divus skaitlus no 1 lidz 20
# programma izvada visus skaitlus no 1 lidz 20, iznemot ievaditos

x = int(input('ievadi pirmo skaitli '))
while x < 1 or x > 20:
    x = int(input('ievadi pareizu pirmo skaitli '))
y = int(input('ievadi otro skaitli '))
while y < 1 or y > 20:
    y = int(input('ievadi pareizu otro skaitli '))

for i in range(1, 21):
    if i != x and i != y:
        print(i)
