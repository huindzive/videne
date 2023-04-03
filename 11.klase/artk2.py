
x=int(input('ievadiu: '))
one=x%10
dos=((x - one)%100)/10
tres=((x-one-(dos*10))%1000)/100
print(one+dos+tres)
