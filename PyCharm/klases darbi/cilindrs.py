
# grupā bija Artūrs, Toms, Mārtiņš un Mārcis M.

import math

pi = math.pi
y = int(input(' ja ir interese par cilindra tilpumu ievadi 1\n ja ir interese par cilindra virsmas laukumu ievadi 2\n'))
if y != 1 and 2 != y:
    print('ir vievadīts nepareizs izvēles cipars')
else:
    if y == 1:
        x = int(input(' ja ir zināms rādiuss un tilpums ievadi 1\n ja ir zināms tilpums un augstums ievadi 2\n ja ir zināms rādiuss un augstums ievadi 3\n'))

        if x != 1 and x != 2 and x != 3:
            print(' ir ievadīts nepareizs izvēles cipars')
        else:
            if x == 1:
                r = int(input(' ievadi rādiusu: '))
                V = int(input(' ievadi tilpumu: '))
                h = V / (pi * (r ** 2))
                print('augstums: ', h)
            elif x == 2:
                V = int(input(' ievadi tilpumu: '))
                h = int(input(' ievadi augstumu: '))
                r = math.sqrt(V / (pi * h))
                print(' rādiuss: ', r)
            elif x == 3:
                h = int(input(' ievadi augstumu: '))
                r = int(input(' ievadi rādiusu: '))
                V = pi * (r ** 2) * h
                print(' tilpums: ', V)
    elif y == 2:
        z = int(input(" ja ir zināms rādiuss un pilnas virsmas laukums ievadi 1\n ja ir zināms pilnas virsmas laukums un augstums ievadi 2\n ja ir zināms rādiuss un augstums ievadi 3\n "))
        if z != 1 and z != 2 and z != 3:
            print(' ir ievadīts nepareizs izvēles cipars')
        else:
            if z == 1:
                R = int(input(' ievadi rādiusu: '))
                Spv = int(input(' ievadi pilnas virsmas laukumu: '))
                Spam = pi * (R**2)
                H = (Spv - (2*Spam)) / (2 * pi * R)
                print('augstums:',H )
            elif z==2:
                Spv = int(input(' ievadi pilnas virsmas laukumu'))
                H = int(input(' ievadi augstumu: '))
                R = Spv / H / 4 / pi
                print('rādiuss:', R)
            elif z == 3:
                R = int(input(' ievadi rādiusu: '))
                H = int(input(' ievadi augstumu: '))
                Spv = (H * 2 * pi * R) + 2 * (pi * (R ** 2))
                print('pilnas virsmas laukums: ', Spv)


#S pam = S rinķim = pi * (R ** 2)
#S sānu = 2 * pi * R * H
# Spv = 2 * pam + S sānu