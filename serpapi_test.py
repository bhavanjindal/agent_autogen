

from langchain.utilities import SerpAPIWrapper
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("SERPAPI_API_KEY")

search = SerpAPIWrapper()

print(search.run("obama's first name ?"))