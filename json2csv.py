import requests
import json
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
data_dict = data[0]

with open('exchange_rates.csv', 'w', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';')
    csvwriter.writerow(['currency', 'code', 'bid', 'ask'])
    for exchange_rates in data_dict['rates']:
        csvwriter.writerow([exchange_rates['currency'], exchange_rates['code'], exchange_rates['bid'], exchange_rates['ask']])



'''
currency_list = []
for exchange_rates in data_dict['rates']:
    currency_list.append(exchange_rates['code'])

print(currency_list)
'''