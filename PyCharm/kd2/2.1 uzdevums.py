x = int(input('ievadi trīsciparu skaitli'))
if 100 <= x <= 999:
    trešais = x % 10
    otrais = (x % 100 - trešais)/10
    pirmais = (x % 1000 - otrais * 10 - trešais)/100
    skaitlis = trešais + otrais + pirmais
    print(skaitlis)

else:
    print('netika ievadīts pareizs skaitlis')