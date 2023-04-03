x=float(input('ievadi x'))
y=float(input('ievadi y'))

if x>0 and y>0:
    print('punkts atrodas 1. kvadrantā')
elif x<0 and y>0:
    print('punkts atrodas 2. kvadrantā')
elif x<0 and y<0:
    print('punkts atrodas 3. kvadrantā')
elif x>0 and y<0:
    print('punkts atrodas 4. kvadrantā')
else:
    print('punkts ir uz taisnes')
if 2*y==6*x-7:
    ('punkts pieder taisnei')