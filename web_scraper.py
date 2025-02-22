import requests
import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup

# ---------------- STOCK PRICE SCRAPER ----------------
def get_stock_prices(stock_symbols):
    stock_data = {}
    for stock in stock_symbols:
        ticker = yf.Ticker(stock)
        price = ticker.history(period="1d")["Close"].iloc[-1]  # Get latest closing price
        stock_data[stock] = price
    return stock_data

# ---------------- WEATHER SCRAPER ----------------
def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Failed to fetch weather data"

# ---------------- NEWS SCRAPER ----------------
def get_news_headlines():
    URL = "https://techcrunch.com/"  # Example: Tech News
    response = requests.get(URL)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.find_all("h2")  # Find all <h2> headlines
        return [headline.get_text().strip() for headline in headlines[:5]]  # Get top 5 news
    else:
        return ["Failed to fetch news"]

# ---------------- RUN SCRAPERS ----------------
if __name__ == "__main__":
    stock_symbols = ["AAPL", "GOOGL", "TSLA", "MSFT", "AMZN"]
    city = "Bangalore"

    # Get data
    stock_prices = get_stock_prices(stock_symbols)
    weather = get_weather(city)
    news_headlines = get_news_headlines()

    # Save to CSV
    df_stocks = pd.DataFrame(stock_prices.items(), columns=["Stock", "Price"])
    df_weather = pd.DataFrame([[city, weather]], columns=["City", "Weather"])
    df_news = pd.DataFrame(news_headlines, columns=["Headline"])

    # Write to CSV
    df_stocks.to_csv("stock_prices.csv", index=False)
    df_weather.to_csv("weather_data.csv", index=False)
    df_news.to_csv("news_headlines.csv", index=False)

    # Print results
    print("✅ Stock Prices:", stock_prices)
    print("✅ Weather:", weather)
    print("✅ News Headlines:")
    for news in news_headlines:
        print(" -", news)

    print("✅ All data saved to CSV files!")
