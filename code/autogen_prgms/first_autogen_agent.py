
# from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json


# load_dotenv()
config_list = config_list_from_json(env_or_file="/Users/bhavanjindal/PycharmProjects/agents_autogen/OAI_CONFIG_LIST")
assistant = AssistantAgent(name="assistant", llm_config={"config_list": config_list})
userproxy = UserProxyAgent(name="userproxy", code_execution_config={"work_dir": "coding"})


userproxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")

