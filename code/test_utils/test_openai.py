from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI


from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

"""######### Using langchain SDK to hit OpenAI LLM model #############"""

# llm = OpenAI(openai_api_key= api_key, model_name='text-davinci-003', temperature=1, max_tokens=512)

# output = llm('explain quantum computing in one sentence')
# print(output)

"""###### you can use generate method as well .... and ask more than one question too"""

# output = llm.generate(['what is the total area of hyderabad', "what is salman khan's latest movie"])
#
# # print(len(output.generations))
# # print(output.generations[0][0].text)
#
#
# for o in output.generations:
#     print(o[0].text)

"""############## Using API method of hitting OpenAI LLM #########"""

import requests

headers = {
    "Authorization": f"Bearer {api_key}"
}

"""#sending a POST request using the v1 GPT /completions API with the requied headers and prompt from user"""
response = requests.post(
    "https://api.openai.com/v1/engines/gpt-3.5-turbo-instruct/completions",
    headers=headers,
    json={
        "prompt": "Write a Python function to calculate the factorial of a number.",
        "max_tokens": 100
    }
)

print(response.json())