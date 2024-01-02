

from langchain.llms import OpenAI
# from langchain.agents import create_spark_sql_agent
from langchain_experimental.agents.agent_toolkits import create_spark_dataframe_agent
from pyspark.sql import SparkSession
from dotenv import load_dotenv

load_dotenv()

spark = SparkSession.builder.getOrCreate()
csv_file_path = "/Users/bhavanjindal/PycharmProjects/agents_autogen/data/titanic.csv"
df = spark.read.csv(csv_file_path, header=True, inferSchema=True)
# df.show()

agent = create_spark_dataframe_agent(llm=OpenAI(temperature=0), df=df, verbose=True)
# agent.run("how many rows are there?")
agent.run("who purchased the cheapest ticket and who purchases the most expensive ticket and for how much ?")