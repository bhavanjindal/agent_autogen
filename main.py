
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json


config_list = config_list_from_json('OAI_CONFIG_LIST')

assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
user_proxy.initiate_chat(assistant, message="plot a chart of TSLA stock price change YTD.")

