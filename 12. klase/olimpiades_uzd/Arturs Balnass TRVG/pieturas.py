z = [1,2,3,4,5,6,7]
s = [8,9,10,11]
bbilet = 0
abilet = 0
braukts = 1
braucieni = int(input("braucieni: "))
start = int(input('sākums: '))
end = int(input('beigas: '))
if start >= 1 and start <=11 and end >= 1 and end <=11 and start != end:
    while braucieni != braukts:
        if start >= 1 and start <=11 and end >= 1 and end <=11 and start != end:
            start = int(input('sākums: '))
            end = int(input('beigas: '))
            if z.count(start) == 1:
                if z.count(end) == 1:
                    braukts+=1
                elif s.count(end) == 1:
                    bbilet+=1
                    braukts+=1

            elif s.count(start) == 1:
                if z.count(end) == 1:
                    abilet+=1
                    braukts+=1
                elif s.count(end) == 1:
                    braukts+=1
        else:
            print("nav pareizi dati")


        

print(abilet,bbilet)
