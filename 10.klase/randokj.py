import random from randint
a=random.randint(1,100)
sk=int(input("ievadi skaitli no 1 līdz 100"))
if sk>a:
    print("Tu uzvarēji")
elif sk<a:
    print("Tu zaudēji")
else :
    print("neizšķirts")