import requests
from dotenv import load_dotenv
import os
load_dotenv()

api_key=os.getenv("API_KEY")

print(f"{api_key}")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":api_key
}

#FETCH YESTERDAY STOCK PRICE
res = requests.get(STOCK_ENDPOINT,params=stock_params).json()["Time Series (Daily)"]

res_list = [value for (key,value) in res.items()]
yesterday_closing = float(res_list[0]["4. close"])
yesterday_opening = float(res_list[0]["1. open"])
variation_percentage = round(((yesterday_closing - yesterday_opening) / yesterday_opening) * 100, 2)
print(yesterday_closing)
print(yesterday_opening)
print(f"{variation_percentage} %")