import requests
from bs4 import BeautifulSoup

URL = 'https://rezka.ag/animation/?utm_source=canva&utm_medium=iframely'
HEADERS = {
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image"
                     "/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/114.0.0.0 Safari/537.36"
}


def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    return response


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div",
                          class_="b-content__inline_item",
                          limit=10
                          )
    parserd_data = []
    for item in items:
        parserd_data.append({
            "title": item.find("div", class_="b-content__inline_item-link").getText().strip(),
            "url": item.find("a").get('href'),
            "image": item.find("img").get("src")
        })

    return parserd_data


def parser():
    html = get_html(URL)
    parsed_data = get_data(html.text)
    return parsed_data
