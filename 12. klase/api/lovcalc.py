import requests

url = "https://love-calculator.p.rapidapi.com/getPercentage"

m=input("ievadi savu vārdu: ")
n=input("ievadi mīļotā vārdu: ")

querystring = {"sname":m,"fname":n}

headers = {
	"X-RapidAPI-Key": "092d095284mshf1f625d9d5b639ep167dbbjsn288e3836d4c3",
	"X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()["precentage"]

print(data)