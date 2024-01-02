
import yfinance as yf


def get_stock_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='7d')
    # return round(todays_data['Close'][0], 2)
    return todays_data

print(get_stock_price('AAPL'))