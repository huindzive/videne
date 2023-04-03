pk1=float(input('ievadi savus punktus'))
pk2=float(input('ievadi maksimālo punktu'))
print(pk1, '/', pk2)
print(pk1/pk2*100, '%')
if pk1/pk2*100>0 and pk1/pk2*100<10:
    print('Tava atzime ir 1')
elif pk1/pk2*100>=11 and pk1/pk2*100<21:
    print('Tava atzime ir 2')
elif pk1/pk2*100>=21 and pk1/pk2*100<35:
    print('Tava atzime ir 3')
elif pk1/pk2*100>=35 and pk1/pk2*100<50:
    print('Tava atzime ir 4')
elif pk1/pk2*100>=50 and pk1/pk2*100<60:
    print('Tava atzime ir 5')
elif pk1/pk2*100>=60 and pk1/pk2*100<70:
    print('Tava atzime ir 6')
elif pk1/pk2*100>=70 and pk1/pk2*100<80:
    print('Tava atzime ir 7')
elif pk1/pk2*100>=80 and pk1/pk2*100<88:
    print('Tava atzime ir 8')
elif pk1/pk2*100>=88 and pk1/pk2*100<96:
    print('Tava atzime ir 9')
elif pk1/pk2*100>=96 and pk1/pk2*100<=100:
    print('Tava atzime ir 10')
elif pk1/pk2*100>100:
    print('tev ir nepareizi sarēķināti punkti')
else:
    print('Tev ir NV')