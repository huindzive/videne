x = int(input('ievadi skaitli: '))
if x>10:
    print('lielaks')
elif x==10:
    print('ir 10')
else:
    print('nav lielaks')

#programma kas ļauj iewvadīt skaitļus līdz tiek ievadīta 0

x=int(input('ievadi skaitļus'));
while x!=0:
    x=int(input('ievadi skaitļus'))

#programma kas izvada visus pozitīvus nepāra skait;us kas mazāki par 20

for i in range (1,21,2): # <- sakuums beigas solis
    print(i)

for i in range(0,21,1):
    if 2%2 != 0:
        print(i)

#masivi

m = [1,4,9,4,5]

for i in range (len(m)):
    print(i,m[i])


# divdimensionālie masīvi

dd = [[14,13,5,7,8],
    [11,6,5,7,4],
    [4,5,23,8,5],
    [5,7,8,98,1],
    [7,41,5,85,51]
]

#simbolu virknes

teikums = 'Labrīt, Deivid!'

print(len(teikums))
print(teikums.count(' ') + 1)
vardi = teikums.split(' ')
print(len(vardi))

jauns = []
for vards in vardi:
    if len(vards) > 0:
        jauns.append(vards)
print(jauns)

text = 'TukumaRainaValstsGimnazija'

for char in text:
    if ord(char) > 64 and ord(char) < 91:
        print(' ', end=' ')
        print(char,end='')
    else:
        print(char,end='' )
    
text =   'tukuma raina valsts gimnazija'
temp = 0
i = 0
new = ""

while i < len(text):
    if temp==i:
        new += chr(ord(text[i]) - 32)
    elif text[i] == " ":
        temp = i + 1
        new += text[i]
    else:
        new += text[i]
    i +=1
print(new)
    

def summa(n):
    sum = 0
    while n>0:
        sk = n % 10
        n=(n-sk) // 10
        sum+=sk
    return sum

print(summa(123))

def otradi(n):
    sum = 0
    while n>0:
        sk = n % 10
        n=(n-sk) // 10
        sum = sum * 10 + sk
    return sum

print(otradi(123))



def masivsNo(n):
    m = []
    while n>0:
        sk = n % 10
        n=(n-sk) // 10
        m.insert(0,sk)
    return m
print(masivsNo(123))


def paraskaits(masivs):
    skaits = 0
    for elem in masivs:
        if elem % 2 == 0:
            skaits += 1
    return skaits

print(paraskaits([2,5,3,6,7]))


def parbaude(masivs):
    for i in masivs:
        if masivs[i] < masivs[i+1]:
            return True
        # elif masivs[i] > masivs[i+1]:
        else:
            return False

print(parbaude([1,2,3,4,5,6]))
