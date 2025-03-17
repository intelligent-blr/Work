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


def get_next_page(soup: bs4.BeautifulSoup) -> str:
    a = soup.select_one("div.pager > a")
    return f'{BASE_URL}{a["href"]}' if a else None


def get_post_data(post) -> dict:
    data = {
        'title': post.select_one("h2 span.serp-item__title-link").text,
        'url': post.select_one("h2 a.bloko-link")["href"],
        'salary': {'min': None, 'max': None, 'salary': None, 'currency': None},
        'organization': {
            'name': post.select_one('span[class^="company-info-text"]').text,
            'url': BASE_URL + post.select_one('div.vacancy-serp-item__meta-info a')['href']},
        'site_url': 'hh.ru',
        'vacancy': request,
    }
    salary = post.select_one('div.vacancy-serp-item__sidebar span')
    # data = clear_salary(salary.text if salary else None, data)
    return data


def main():
    for soup in get_page(url):
        data_posts = soup.select('div.vacancy-search-item__card')
        data = [get_post_data(post) for post in data_posts]

        sleep(1.5)


main()
