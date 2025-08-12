from playwright.async_api import async_playwright
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from dotenv import load_dotenv
import os
import requests
from langchain.agents import Tool
from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_experimental.tools import PythonREPLTool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_google_community import GmailToolkit

load_dotenv(override=True)
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_url = "https://api.pushover.net/1/messages.json"
serper = GoogleSerperAPIWrapper()
gmail_toolkit = GmailToolkit()


async def get_playwright_tools():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
    return toolkit.get_tools(), browser, playwright


def push(text: str):
    """Send a push notification to the user"""
    requests.post(pushover_url, data={"token": pushover_token, "user": pushover_user, "message": text})
    return "success"


def get_push_tools():
    push_tool = Tool(
        name="send_push_notification",
        func=push,
        description="Use this tool when you want to send a push notification"
    )
    return [push_tool]


def get_file_tools():
    toolkit = FileManagementToolkit(root_dir="sandbox")
    return toolkit.get_tools()


def get_search_tools():
    search_tool = Tool(
        name="search",
        func=serper.run,
        description="Use this tool when you want to get the results of an online web search"
    )
    return [search_tool]


def get_wikipedia_tools():
    wikipedia = WikipediaAPIWrapper(wiki_client=WikipediaQueryRun)
    wiki_tool = WikipediaQueryRun(api_wrapper=wikipedia)
    return [wiki_tool]


def get_gmail_tools():
    return gmail_toolkit.get_tools()


def get_python_repl_tools():
    return [PythonREPLTool()]


async def get_all_tools():
    file_tools = get_file_tools()
    push_tools = get_push_tools()
    search_tools = get_search_tools()
    wikipedia_tools = get_wikipedia_tools()
    gmail_tools = get_gmail_tools()
    python_repl_tools = get_python_repl_tools()

    return file_tools + push_tools + search_tools + wikipedia_tools + gmail_tools + python_repl_tools
