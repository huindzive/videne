with open("dictionary2.txt") as f:
    line1 = f.readline()
    vertibas = line1.split()

    pSkaits = (int(vertibas[0]))
    zPieturas = int(vertibas[1])
    posmi = int(vertibas[2])

    print(pSkaits,zPieturas,posmi)

    pieturas = {i:[] for i in range(1,12)}
    print(pieturas)

    dic = {}
    dic2 = {
        '3':'10',
        '6':'9',
        '9':'0'
    }
    #faila atveshana
    # with open("dictionary1.txt") as f:

    #     lines = f.readlines()
    #     for line in lines:
    #         key_value = line.split()
    #         print(key_value)
    #         dic[key_value[0]] = key_value[1]

    #     print(dic2[dic['6']])
    #     for key in dic:
    #         if dic[key] in dic2:
    #             print(dic2[dic[key]])

    for _ in range(posmi):
            #nolasa vienu rindinu
        line = f.readline()
            # saalam rindinu pa atstarpem lai iegutu atseviski katru vertibu rindina
        line = line.split()
            #iegustam katras vertibas skaitlisko vertibu
        line[0] = int(line[0])
        line[1] = int(line[1])

        pieturas[line[0]].append(line[1])
        pieturas[line[1]].append(line[0])

    # for key in pieturas:
    #     print(key, pieturas[key])

    zala = {}
    sarkana = {}
    for key in pieturas:
        if key > 7:
            sarkana[key] = pieturas[key]
        else:
            zala[key] = pieturas[key]

    # zalas = {i:pieturas[i] for i in range(1,8)}
    # sarkanas = {i:pieturas[i] for i in range(8,12)}

    print(zala)
    print(sarkana)