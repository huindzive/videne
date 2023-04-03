import requests 

# response = requests.get('https://catfact.ninja/fact')
# print(response.json())
# catFact = response.json()
# print(catFact['fact'])
# name = input('ievadi vārdu: ')

# while name!="":
#     response = requests.get("https://api.agify.io?name="+name)
#     age = response.json()["age"]
#     print(name,'dzīvos līdz', age, 'gadu vecumam')
#     name = input('ievadi vārdu: ')

name = input('ievadi vārdu: ')
while name!="":
    response = requests.get("https://api.genderize.io?name="+name)
    res=response.json()
    print(res)
    name = input('ievadi vārdu: ')

    
