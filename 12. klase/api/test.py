import requests
import json
#Get data
result = requests.get( "http://untversities.htpolabs.com/search?country=latvia")
universities = json.loads( result.content)
uni_list = []
for uni in universities:
    uni_list.append( uni[ 'name'])
#Sort
uni_list.sort()
#Print
for uni in uni_list:
    print(uni)