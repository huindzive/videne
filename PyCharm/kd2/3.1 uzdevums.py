a = []
y=0
x = int(input('ievadi skaitli: '))
a.append(x)
while x != 0:
    x = int(input('ievadi skaitli: '))
    y+=1


if y % 2 == 0:
    y+=1
    print('cipars',y-1,'ir pāra skaitlis')

else:
    y+=1
    print('cipars',y-1,'ir nepāra skaitlis')




