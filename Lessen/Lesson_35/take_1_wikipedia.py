import requests


response = requests.get("https://en.wikipedia.org/wiki/Tree")
print(response.status_code)  # Выводит код состояния ответа (200 - успешный запрос)
print(response.headers)  # Выводит заголовки

print(1)

data = response.text

for teg in data.split('\n'):
    if teg.startswith('<p>'):
        print(teg)

print(1)