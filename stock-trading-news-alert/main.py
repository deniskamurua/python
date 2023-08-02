import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"


COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# api key from alphavantage website

STOCK_API_KEY = "SDGSDSDBSDSDSDGWE"
NEWS_API_KEY = "VSBDFSEJRVZBNJRDF"   # from newsapi.org
TWILIO_SID = "AC36829a64a593edf5098197a2d0ebb9f0"
TWILIO_AUTH_TOKEN = "19a0ba19ebbd72a9c6e9e6383d5b8270"



# get yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
# data is a dictionary very large which we have to convert to a list

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# day before yesterday's data
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# positive difference between them use abs() to get positive
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

# percentage difference
diff_percent = (difference / float(yesterday_closing_price)) * 100

if diff_percent > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    # use python slicing to get the first 3 articles
    three_articles = articles[:3]
    print(articles)

    # create a list of the first 3 article headline and description

    formatted_articles = [f"Headline: {article['title']},\nBrief: {article['description']}"
                          for article in three_articles]

    # sending the message via twilio

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # Sending each article seperate via twilio
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+12053509049",
            to="+254712435678"
        )

