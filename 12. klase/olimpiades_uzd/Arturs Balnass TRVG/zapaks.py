a = [] # ievadītā virkne
ac = [] # garākā virkne kas bija
skaitli = int(input("ievadi skaitļu skaitu: "))

for i in range(skaitli):
    ievad = int(input("ievadi virkni pa vienam: "))
    a.append(ievad)

print(a)

for i in range(len(a)):
    if i == 0:
        ac.append(a[i])
    elif i > 0:
        if i % 2 == 0:
            if len(a) > 2:
                if i==0:
                    if a[i] > a[i-1]:
                        ac.append(a[i])
                    else:
                        a.remove(a[0])
                        for i in range(len(a)-1):
                            if i == 0:
                                ac.append(a[i])
                            elif i > 0:
                                if i % 2 == 0:
                                    if a[i] > a[i-1]:
                                        ac.append(a[i])
                                    else:
                                        a.remove(a[0])

                                elif i % 2 == 1:
                                    if a[i] < a[i-1]:
                                        ac.append(a[i])
                                    else:
                                        a.remove(a[0])
                
            else:
                print(ac,len(ac))                        

        elif i % 2 == 1:
            if len(a) > 2:
                if i == 0:
                    ac.append(a[i])
                else:
                    if a[i] > a[i-1]:
                        ac.append(a[i])
                    else:
                        a.remove(a[0])
                        for i in range(len(a)-1):
                            if i == 0:
                                ac.append(a[i])
                            elif i > 0:
                                if i % 2 == 0:
                                    if a[i] > a[-1]:
                                        ac.append(a[i])
                                    else:
                                        a.remove(a[0])

                                elif i % 2 == 1:
                                    if a[i] < a[i-1]:
                                        ac.append(a[i])
                                    else:
                                        a.remove(a[0])
            else:
                print(ac,len(ac))                        
            

print(ac)