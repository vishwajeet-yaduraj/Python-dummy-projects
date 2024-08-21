import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API")
NEWS_API = "https://newsapi.org/v2/everything"

account_sid = os.getenv("TWILIO_SID")
auth_token = "5c87c8ddc6843fec2ae64df57564212d"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": stock_api_key
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
data = [value for key, value in data.items()]
# print(data)

yesterday_data = data[0]
yesterday_closing_price = yesterday_data['4. close']

day_before_data = data[1]
day_before_closing_price = day_before_data['4. close']

difference = abs(float(yesterday_closing_price) - float(day_before_closing_price))
diff_percent = (difference / float(yesterday_closing_price)) * 100

print(diff_percent)

if diff_percent > 5:
    parameter = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(url=NEWS_API, params=parameter)
    top_three_articles = news_response.json()["articles"][:3]
    # print(top_three_articles)

    formatted_article = [f"Headline: {article['title']}\n Brief: {article['description']}" for article in
                         top_three_articles]
    print(formatted_article)
    client = Client(account_sid, auth_token)
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_='+12085409435',
            to= os.getenv('PHONE')
        )
