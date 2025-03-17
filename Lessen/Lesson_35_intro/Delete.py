from bs4 import BeautifulSoup
import requests

url = 'http://mignews.com/mobile'
page = requests.get(url)
print(page.status_code)

new_news = []
news = []

soup = BeautifulSoup(page.text, "html.parser")

news = soup.findAll('a', class_='lenta')

for news_item in news:
    if news_item.find('span', class_='time2 time3') is not None:
        new_news.append(news_item.text)

for data in new_news:
    print(data)