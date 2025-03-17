import requests
import bs4
from time import sleep

request = input('Введите запрос на вакансию: ').strip().replace(' ', '+')

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
BASE_URL = 'https://hh.ru'
url = f'https://hh.ru/search/vacancy?text={request}'


def get_page(url):
    while url:
        print(url)
        response = requests.get(url, headers=headers)
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        yield soup
        url = get_next_page(soup)
        print(url)


def get_next_page(soup: bs4.BeautifulSoup) -> str:
    a = soup.select_one('ul[class^="magritte-number-pages-container"] a[data-qa="pager-next"]')
    return f'{BASE_URL}{a["href"]}' if a else None


def get_post_data(post) -> dict | None:
    try:
        salary = post.select_one('div[class^="wide-container"] > div[class^="compensation-labels"] span[class^="magritte-text"]')
        data = {
            'title': post.select_one('span[data-qa="serp-item__title-text"]').text,
            'url': post.select_one('a[data-qa="serp-item__title"]')["href"],
            # 'salary': {'min': None, 'max': None, 'salary': None, 'currency': None},
            'salary': salary.text if salary else None,
            'tags': [i.text for i in post.select('div div[class^="wide-container"] div[class^="magritte-tag"] span')],
            'company': {
                'name': post.select_one('div[class^="company-name-badges-container"] a[data-qa^="vacancy-serp__vacancy-employer"]').text,
                'url': BASE_URL + post.select_one('div[class^="company-name-badges-container"] a[data-qa^="vacancy-serp__vacancy-employer"]')['href'],
                },
            'city': post.select_one('div[class^="wide-container"] > div[class^="wide-container"] > span[data-qa="vacancy-serp__vacancy-address"]').text,
            'site_url': 'hh.ru',
            'vacancy': request,
        }
        return data
    except AttributeError:
        return None
    