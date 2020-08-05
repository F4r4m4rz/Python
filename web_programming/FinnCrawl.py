
import webbrowser
import requests
from bs4 import BeautifulSoup
import urllib.parse as up
from fake_useragent import UserAgent


def find_jobs(title='C# developer'):
    print('Searching ...')
    _title = up.quote(title)
    url = "https://www.finn.no/job/fulltime/search.html?q={}&sort=1".format(_title)
    res = requests.get(url=url)
    with open('finn1.html', 'wb') as out_file:
        for data in res.iter_content(10000):
            out_file.write(data)
    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.find_all('div', {'class': 'ads__unit__content__keys'})
    soup.
    # links = list(soup.select("banners__topboard"))[:5]
    print(len(links))
    for link in links:
        print(link)


if __name__=='__main__':
    find_jobs('C# developer')