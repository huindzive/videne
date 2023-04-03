import random
dators=random.randint(1,100)
skaits=0
lietotajs=0
while lietotajs!=dators:
    lietotajs=int(input('ievadi skaitli'))
    skaits=skaits+1
    if dators<lietotajs:
        print('skaitlis ir par lielu')
    elif dators>lietotajs:
        print('skaitlis ir par mazu')
print('uzminēji ar ', skaits,'. reizi')