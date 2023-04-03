x=int(input('cik skaitluys ievadisi'))
bc=0
for i in range(x):
    a=int(input('ievadi skaitli'))
    if a>=10 and a<=99:
        bc=bc+1
    elif a>=-99 and a<=-10:
        bc=bc+1
print(bc)