from playwright.async_api import async_playwright
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from dotenv import load_dotenv
import os
import requests
import wikipediaapi
from langchain.agents import Tool
from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_experimental.tools import PythonREPLTool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper  

# Load env
load_dotenv(override=True)
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_url = "https://api.pushover.net/1/messages.json"
serper = GoogleSerperAPIWrapper()

async def playwright_tools():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
    return toolkit.get_tools(), browser, playwright

def push(text: str):
    requests.post(pushover_url, data={"token": pushover_token, "user": pushover_user, "message": text})
    return "success"

def create_push_tool():
    return Tool(
        name="send_push_notification",
        func=push,
        description="Use this tool when you want to send a push notification"
    )

def create_file_tools():
    toolkit = FileManagementToolkit(root_dir="sandbox")
    return toolkit.get_tools()

def create_search_tool():
    return Tool(
        name="search",
        func=serper.run,
        description="Use this tool when you want to get the results of an online web search"
    )

def create_wiki_tool():
    wiki_client = wikipediaapi.Wikipedia('en')
    wikipedia = WikipediaAPIWrapper(wiki_client=wiki_client)
    return WikipediaQueryRun(api_wrapper=wikipedia)

def create_python_repl_tool():
    return PythonREPLTool()

async def get_all_tools():
    file_tools = create_file_tools()
    push_tool = create_push_tool()
    search_tool = create_search_tool()
    wiki_tool = create_wiki_tool()
    python_repl_tool = create_python_repl_tool()
    
    return file_tools + [push_tool, search_tool, python_repl_tool, wiki_tool]
