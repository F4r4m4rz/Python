
from newsapi import NewsApiClient
import pprint

_NEWS_API = NewsApiClient(api_key= 'e444c2db750d4ae6b6650a96e95f25ed')


def my_get_top_headlines(topic='iran', source=None, category=None, language='fa', country='IR'):
    top_headlines = _NEWS_API.get_top_headlines(q=topic)
    pprint.pprint(top_headlines)


if __name__ == '__main__':
    my_get_top_headlines('job')