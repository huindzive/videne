# programma, kas parbauda, vai skaitlis ir pirmsskaitlis
# (prime number)

a = 1
while a == 1:
    x = int(input('ievadi skaitli: '))
    dalitajuSkaits = 0

    if x <= 1:
        print('neder')
    else:
        for i in range(2, x + 1):
            if x % i == 0:
                dalitajuSkaits += 1

        if dalitajuSkaits == 1:
            print('skaitlis ir pirmskaitlis')
        else:
            print('nav pirmskaitlis ', dalitajuSkaits, ' dalitaji')
    a = int(input('ievadi 1, ja velies atkartot! '))
