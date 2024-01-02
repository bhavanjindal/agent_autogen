from typing import Optional, Type

import yfinance as yf
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

def get_stock_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return round(todays_data['Close'][0], 2)

# print(get_stock_price('AAPL'))
# print(get_stock_price('GOOG'))

class StockPriceCheckInput(BaseModel):
    """Input for Stock price check."""

    stockticker: str = Field(..., description="Ticker symbol for stock or index")
class StockPriceTool(BaseTool):
    name = "Get Stock ticker price"
    description = "useful for when you need to find out the price of a stock. you should input the stock ticker used on yfinance api"

    def _run(self, stockticker: str):
        price_response = get_stock_price(stockticker)

        return price_response

    def _arun(self, stockticker: str):
        raise NotImplementedError("This tool does not support async")

    args_schema: Optional[Type[BaseModel]] = StockPriceCheckInput


# stockpricetool = Tool(
#     name="Get Stock ticker price",
#     func=get_stock_price,
# description = "useful for when you need to find out the price of a stock. you should input the stock ticker used on yfinance api"
# )
