from cust_funcs.yfinance_funcs import StockPriceTool
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from dotenv import load_dotenv
from langchain.tools import format_tool_to_openai_function


# def get_stock_price(symbol):
#     ticker = yf.Ticker(symbol)
#     todays_data = ticker.history(period='1d')
#     return round(todays_data['Close'][0], 2)
#
# stockpricetool = Tool(
#     name="Get Stock ticker price",
#     func=get_stock_price,
# description = "useful for when you need to find out the price of a stock. you should input the stock ticker used on yfinance api"
# )


load_dotenv()

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
tools = [StockPriceTool()]
# tools = [StockPriceTool()]
functions = [format_tool_to_openai_function(t) for t in tools]


agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

agent.run("what is the price of google stock ")
