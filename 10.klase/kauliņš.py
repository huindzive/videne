import random
dators=random.randint(1,6)
skaits=1
while dators!=6:
    dators=random.randint(1,6)
    skaits=skaits+1
if dators==6:
    print("kaulinu meti" ,skaits, 'reizes')