# Doti tris skaitli a, b, c, kas ir kvadratvienadojuma koeficienti.
# Atrast kvadratvienadojuma saknes.
import math

a = int(input('ievadi a: '))
b = int(input('ievadi b: '))
c = int(input('ievadi c: '))

dis = b ** 2 - 4 * a * c
x1 = (- b + math.sqrt(dis)) / 2 * a
x2 = (- b - math.sqrt(dis)) / 2 * a

print('x1 = ', x1, ' x2 = ', x2)
print(math.pi)
