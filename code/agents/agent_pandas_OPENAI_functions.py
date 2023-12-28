from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd

load_dotenv()

df = pd.read_csv('/data/titanic.csv')
# print(df.head())
llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=1)

agent = create_pandas_dataframe_agent(llm, df, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)

agent.run("how many rows are there and what is distribution of male and female")


