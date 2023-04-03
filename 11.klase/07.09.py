#programma, kas izdrukā visus skaitļus no 1-9

#for i in range(10):
#    print(i)
#    
#print()
#for j in range(18,35):
    #print(j)
    
#2
    
a = []
x = int(input('ievadi skaitli: '))
while x != 0:
    a.append(x)
    x = int(input('ievadi skaitli: '))

summa = 0
for i in range(len(a)):
    summa += a[i]
print('summa:', summa)

for i in range(len(a)):
    print(a[i], end=' ')
print()

#3

for i in range(len(a)):
    if a[i]%2==0 :
        print(a[i])


#4
for i in range(len(a)-1, -1, -1):
        print(a[i], end=' ')

print()
#5
lielakais = a[0]

for i in range(1, len(a)):
    if a[i] > lielakais:
        if a[i]%2==0:
            lielakais = a[i]
        

print(lielakais)
