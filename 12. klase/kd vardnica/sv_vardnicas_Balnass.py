vieni = {0:'ais', 1:" pirmais",2:' otrais',3:' trešais',4:' ceturtais',5:' piektais',6: ' sestais',7:' septitais',8:' astotais',9:' devitais'}
patsmiti = {0:'desmitais',1:'vienpadsmitais',2:'divpadsmitais',3:'trispadsmitais',4:'cetrpadsmitais',5:'piecpadsmitais',6:'sespadsmitais',7:'septinpadsmitais',8:'astonpadsmitais',9:'devinpadsmitais'}
desmiti = {0:'' ,2:"divdesmit",3:'trisdesmit'}
menesis = {1:'janvaris',2:'februaris',3:'marts',4:'aprilis',5:'maijs',6:'junijs',7:'julijs',8:'augusts',9:'septembris',10:'oktobris',11:'novembris',12:'decembris'}


date = input("skaitlis: ")

datums = date.split('.')

d = int(datums[0])
m = int(datums[1])

diena = [d,m]
if d>31 or m>12:
    print("tu ir tups")
else:
    if m == 2 and d<= 28:
        if d > 9 and d<20:
            print(patsmiti[d%10] + ' '+menesis[m])
        else:
            print(desmiti[d//10] + vieni[d%10] + ' '+ menesis[m])
    elif [4,6,9,11].count(m) == 1 and d<=30:
        if d > 9 and d<20:
            print(patsmiti[d%10] + ' '+menesis[m])
        else:
            print(desmiti[d//10] + vieni[d%10] + ' '+ menesis[m])
    elif [1,3,5,7,8,10,12].count(m) == 1 and d <=31:
        if d > 9 and d<20:
            print(patsmiti[d%10] + ' '+menesis[m])
        else:
            print(desmiti[d//10] + vieni[d%10] + ' '+ menesis[m])
    else:
        print('tu ir dārzenis')
