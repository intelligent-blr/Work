import requests

# Напишите функцию get_response(url), которая отправляет GET-запрос
# по заданному URL-адресу и возвращает объект ответа.
# Затем выведите следующую информацию об ответе:
# - Код состояния(status code)
# - Текст ответа(response text)
# - Заголовки ответа(response headers)


def get_response(url):
    response = requests.get("https://"+url)
    print(response.status_code)
    print(response.text)
    print(response.headers)


url = input("Введите адрес сайта: ")

get_response(url)