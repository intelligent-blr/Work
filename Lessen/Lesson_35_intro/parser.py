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
        # url = get_next_page(soup)
        # print(url)


def main():
    for soup in get_page(url):
        data_posts = soup.select('div[data-qa^="vacancy-serp__vacancy"]')
        # data = [get_post_data(post) for post in data_posts]

        sleep(1.5)


main()
