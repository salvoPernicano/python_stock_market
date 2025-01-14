import requests
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("API_KEY")

print(f"{api_key}")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key
}


response = requests.get(STOCK_ENDPOINT, params=stock_params)


if response.status_code != 200:
    print("Errore nella richiesta all'API")
    exit()


res = response.json().get("Time Series (Daily)")


if not res:
    print("Dati non disponibili")
    exit()


res_list = [value for (key, value) in res.items()]
yesterday_closing = float(res_list[0]["4. close"])
yesterday_opening = float(res_list[0]["1. open"])


variation_percentage = round(((yesterday_closing - yesterday_opening) / yesterday_opening) * 100, 2)


print(f"Prezzo di apertura di ieri: {yesterday_opening:.2f}")
print(f"Prezzo di chiusura di ieri: {yesterday_closing:.2f}")
print(f"Variazione percentuale: {variation_percentage}%")
