simti = {'0':'',"1": "simtu","2": 'divi simti',"3":'tris simti','4':'cetri simti','5':'pieci simti','6':'sesi simti','7':'septini simti','8':'astoni simti','9':'devini simti'}
desmiti = {'0':'','2': "divdesmit",'3':"trisdesmit",'4':'cetrdesmit','5':'piecdesmit','6':'sesdesmit','7':'septindesmit','8':'astondesmit','9':'devindesmit'}
vieni = {'0':'', '1':"viens",'2':'divi','3':'tris','4':'cetri','5':'pieci','6':'sesi','7':'septini','8':'astoni','9':'devini'}
patsmiti = {'0':'desmit','1':'vienpadsmit','2':'divpadsmit','3':'trispadsmit','4':'cetrpadsmit','5':'piecpadsmit','6':'sespadsmit','7':'septinpadsmit','8':'astonpadsmit',"9":'devinpadsmit'}

x = input('skaitlis: ')
xnum = int(x)
if len(x) == 1:
    print(vieni[x[0]])
elif len(x) == 2:
    if x[0] == '1':
        print(patsmiti[x[1]])
    else:
        print(desmiti[x[0]]+ ' '+ vieni[x[1]])
elif len(x) == 3:
    if x[1] == '1':
        print(simti[x[0]]+' '+patsmiti[x[2]])
    else:
        print(simti[x[0]]+' '+desmiti[x[1]]+' '+vieni[x[2]])
else:
    print('ievadits nepareizs skaitlis,dobermani')


num = int(input('ievadi: '))
s = []

while num>0:
    p=num%10
    s.insert(0,p)
    num//=10

while len(s) < 3:
    s.insert(0,0)

print(s)

if s[1]==1:
    print(simti[s[1]] + ' ' + patsmiti[s[3]])
else:
    print(simti[s[0]] + ' ' +desmiti[s[1]] + ' '+ vieni[s[2]])
