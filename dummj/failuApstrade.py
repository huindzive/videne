# faila atvēršana, nolasīšana

with open("fails.txt") as file:
    persons = file.readlines()
    for i in range(len(persons)):
        persons[i] = persons[i].replace("\n","")
    

    persons.sort(reverse=True)
    print(persons)

    words=[]

    for person in persons:
        words += person.split()

    print(words)