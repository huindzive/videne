# Dotas trīs vārdnīcas a, b un c;
# Izveidot vārdnīcu d, kura veidojas triju vārdnīcu slēguma rezultātā - 
# īsceļu no vārdnīcas a atslēgu uz vārdnīcas c tulkojumu.
# Tātad, ja iekš a eksistē w:x, b - x:y, c - y:z, tad iekš d jābūt w:z.
# Vārdnīcu d sakārtot pēc atslēgas un izvadīt uz ekrāna.

a = {'c':'a', 'r':'t', 'y':'e', 'f':'b', 'w':'y', 'k':'j', 'm':'n'}
b = {'e':6, 'b': 7, 'x': 8, 'a':12, 'j':3, 'y':5, 'n':17, 'z':4, 'h':9}
c = {3:'L', 1:'K', 17:'s', 5:'a', 2:'g', 6:'b', 7:'a', 12:'i', 10:'v'}
d = {}

sal1 = {}


for key in a:
    if a[key] in b:
        # print(b[a[key]])
        sal1[key] = b[a[key]]
        # print(sal1)

for key2 in sal1:
    if sal1[key2] in c:
        # print(c[sal1[key2]])
        d[key2] = c[sal1[key2]]
        # print(d)


print(d)


sorted_dic = sorted(d, key=d.get, reverse=True)

print(sorted_dic[:])