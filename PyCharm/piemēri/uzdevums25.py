# Rekursija - funkcijas izsaukums
# pašas darbībā, funkcija izsauc pati sevi.


def faktorials(x):
    if x == 1:
        return x
    else:
        return x * faktorials(x-1)


def rekursija(x):
    if x == 0:
        return x
    else:
        print(x)
        rekursija(x - 1)
    print(x)


rekursija(3)

