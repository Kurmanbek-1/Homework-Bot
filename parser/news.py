import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = 'https://kaktus.media/'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req



def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="Dashboard-Content-Card")
    # pprint(items)
    animes = []
    for item in items:
        anime = {
            'link': item.find('a', class_="Dashboard-Content-Card--image").get('href')

        }
        animes.append(anime)
    return animes
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        animes = []
        for i in range(1,2):
            html = get_html(f'{URL}page/{i}/')
            anime = get_data(html.text)
            animes.extend(anime)

        return anime
    else:
        raise Exception('Errorn parser!')

