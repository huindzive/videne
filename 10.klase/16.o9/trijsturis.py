viens=float(input('ievadi pirmo nogriezni'))
divi=float(input('ievadi otro nogriezni'))
tris=float(input('ievadi trešo nogriezni'))
if viens<(divi+tris) and divi<(viens+tris) and tris<(viens+divi):
    print('strādā')
else:
    print('nestrādā')