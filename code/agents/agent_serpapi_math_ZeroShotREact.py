

from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=1)
tools = load_tools(["serpapi", "llm-math"], llm)
agent_exec = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent_exec.run("what is the average price of a two bhk flat in hyderabad and calculate 20% downpayment for it")

