import math
pi=math.pi
x = int(input('ievadi lielāko rādiusu: '))
y = int(input('ievadi mazāko rādiusu: '))
xS = pi * (x**2)
yS = pi * (y**2)
Sgredz = xS - yS
print('gredzena laukums: ', Sgredz)
