
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
data_dict = data[0]
currency_list = []
for exchange_rates in data_dict['rates']:
    currency_list.append(exchange_rates['code'])


@app.route("/kalkulator/", methods=["GET", "POST"])

def kalkulator():
    items = currency_list

    if request.method == "POST":

        data = request.form
        
        pln_exchange = data.get("pln_exchange")
        currency_choice = data.get('currency_choice')

        for exchange_rates in data_dict['rates']:
            if exchange_rates['code'] == currency_choice:
                res =  float(pln_exchange.replace(',','.')) / exchange_rates['ask']


        writing1 = "Za posiadaną kwotę kupisz"
        writing2 = f"{res:.2f}"
        writing3 = currency_choice

        return render_template("kalkulator.html",  items=items, writing1 = writing1, writing2 = writing2, writing3 = writing3)
        
    

    return render_template("kalkulator.html", items=items)
 


if __name__ == "__main__":
    app.run(debug=True)

    