#rekursija - funkcijas izsaukumi
#pašas darbībā, funkcija

def rekursija(x):
    if x==1:
        return x
    else:
        return x * rekursija(x-1)

print(rekursija(4))

def rekursija2(x):
    if x == 1:
        return x
    print(rekursija(x-1))

rekursija2(4)

# fibončī: 1,1,2,3,5,8,12