from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI


from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key= api_key, model_name='text-davinci-003', temperature=1, max_tokens=512)

output = llm('explain quantum computing in one sentence')
print(output)

# output = llm.generate(['what is the total area of hyderabad', "what is salman khan's latest movie"])
#
# # print(len(output.generations))
# # print(output.generations[0][0].text)
#
#
# for o in output.generations:
#     print(o[0].text)

