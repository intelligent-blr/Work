"""
2. Напишите функцию find_common_words(url_list), которая принимает список URL-адресов
и возвращает список наиболее часто встречающихся слов на веб-страницах.
Для каждого URL-адреса функция должна получить содержимое страницы с помощью запроса
GET и использовать регулярные выражения для извлечения слов.
Затем функция должна подсчитать количество вхождений каждого слова
и вернуть наиболее часто встречающиеся слова в порядке убывания частоты.
"""

import requests
import re
from collections import Counter

def remove_html_tags(html_text):
    plain_text = re.sub(r'<[^>]+>', '', html_text)
    return plain_text.strip()


def find_common_words(url):
    text = requests.get(url).text
    clear_text = remove_html_tags(text)

    words = re.findall(r"\b[a-zA-Zа-яА-ЯёЁ]+\b", clear_text)
    for key, value in Counter(words).most_common(50):
        print(f"{key} {value}")


find_common_words("https://en.wikipedia.org/wiki/Tree")
