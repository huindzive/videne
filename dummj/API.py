import requests

response = requests.get('http://universities.hipolabs.com/search?country=Latvia')
response = response.json()

names =[]
for school in response:
    names.append(school['name'])
names.sort

print(names)