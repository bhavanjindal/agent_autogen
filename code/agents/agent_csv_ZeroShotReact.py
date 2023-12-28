from langchain.agents import agent_types, load_tools, AgentType
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.agents.agent_toolkits import create_spark_sql_agent
from langchain_experimental.agents.agent_toolkits import create_csv_agent

load_dotenv()
llm = OpenAI(temperature=1)

agent = create_csv_agent(llm, '/Users/bhavanjindal/PycharmProjects/agents_autogen/data/titanic.csv', verbose=True, agent_types=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

agent.run('what was the average age of survivors. can you plot that in a line graph ?')





