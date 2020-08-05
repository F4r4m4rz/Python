# Created by sarathkaul on 12/11/19

import requests

_NEWS_API = "https://newsapi.org/v2/everything?source=reuters&sortBy=top&apiKey=e444c2db750d4ae6b6650a96e95f25ed"


def fetch_bbc_news(bbc_news_api_key: str) -> None:
    # fetching a list of articles in json format
    bbc_news_page = requests.get(_NEWS_API).json()
    # each article in the list is a dict
    for i, article in enumerate(bbc_news_page["articles"], 1):
        print(f"{i}.) {article['title']}")


if __name__ == "__main__":
    fetch_bbc_news(bbc_news_api_key="Iran")
