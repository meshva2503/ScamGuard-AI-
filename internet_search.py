import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

def internet_search(max_results: int = 3):
    return tavily_client.search(
        query="latest online scams fraud alerts",
        topic="news",
        max_results=max_results,
        include_raw_content=False,
    )
