
import requests
from utils.config import NEWS_API_KEY

def fetch_wikipedia_summary(topic):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("extract", "")
    return "No Wikipedia data found."

def fetch_news_snippets(keywords):
    url = f"https://api.thenewsapi.com/v1/news/all?api_token={NEWS_API_KEY}&language=en&search={keywords[0]}"
    response = requests.get(url)
    snippets = []
    links = []
    if response.status_code == 200:
        articles = response.json().get("data", [])[:5]
        for article in articles:
            snippets.append(article.get("snippet", ""))
            links.append(article.get("url", ""))
    return snippets, links
