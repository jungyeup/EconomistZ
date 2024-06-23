from langchain_community.utilities.polygon import PolygonAPIWrapper
from langchain_community.tools import PolygonLastQuote, PolygonTickerNews, PolygonFinancials, PolygonAggregates
from dotenv import load_dotenv

load_dotenv()

api = PolygonAPIWrapper()



# Get the last quote for a ticker
quote = PolygonLastQuote(api)
quote.invoke({"ticker": "AAPL"})
# Get the latest news for a ticker
news = PolygonTickerNews(api)
news.invoke({"ticker": "AAPL"})
# Get the financials for a ticker
financials = PolygonFinancials(api)
financials.invoke({"ticker": "AAPL"})
# Get the aggregates for a ticker
aggregates = PolygonAggregates(api)
aggregates.invoke({"ticker": "AAPL"})


import json
import httpx

from phi.assistant import Assistant


def get_poligon(num_stories: int = 10) -> str:
    """Use this function to get top stories from Hacker News.

    Args:
        num_stories (int): Number of stories to return. Defaults to 10.

    Returns:
        str: JSON string of top stories.
    """

    # Fetch top story IDs
    response = httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    story_ids = response.json()

    # Fetch story details
    stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        stories.append(story)
    return json.dumps(stories)

assistant = Assistant(tools=[get_top_hackernews_stories], show_tool_calls=True)
assistant.print_response("Summarize the top stories on hackernews?")