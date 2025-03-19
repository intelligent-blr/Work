import requests
from bs4 import BeautifulSoup

# Сам не делал!

# 1. Напишите программу, которая запрашивает у пользователя URL-адрес
# веб-страницы, использует библиотеку Beautiful Soup для парсинга HTML
# и выводит список всех ссылок на странице.


def get_links(url):
    html = requests.get("https://"+url).text
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    for i in links:
        print(i["href"])


address = input("Введите адрес страницы: ")

get_links(address)

# 2. Напишите программу, которая запрашивает у пользователя URL-адрес
# веб-страницы и уровень заголовков, а затем использует библиотеку
# Beautiful Soup для парсинга HTML и извлекает заголовки нужного
# уровня(теги h1, h2, h3 и т.д.) с их текстом.


def get_headers(url, level):
    html = requests.get("https://"+url).text
    soup = BeautifulSoup(html, "html.parser")
    headers = soup.find_all("h"+level)
    for i in headers:
        print(i)


address = input("Введите адрес страницы: ")
level = input("Введите уровень заголовка: ")

get_headers(address, level)