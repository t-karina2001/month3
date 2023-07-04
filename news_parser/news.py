import requests
from bs4 import BeautifulSoup

URL = 'https://www.securitylab.ru/news/?utm_source=canva&utm_medium=iframely'


def get_html(url):
    response = requests.get(url=url)
    return response


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all(
        "a",
        class_="article-card inline-card",
        limit=10
    )
    parserd_data = []
    for item in items:
        parserd_data.append({
            "title": item.find("h2", class_="article-card-title").string.strip(),
            "url": item.find("a", class_="article-card inline-card")["href"],
            "description": item.find("p").getText.strip(),
            "time": item.find("time").getText().strip()

        })

    return parserd_data


def parser():
    html = get_html(URL)
    parsed_data = get_data(html.text)
    return parsed_data
