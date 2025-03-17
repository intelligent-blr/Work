from db import create_database_and_tables, insert_vacancy
from script import get_page, get_post_data, url


def main():
    create_database_and_tables()  # Создаем базу данных и таблицы, если их нет
    for soup in get_page(url):
        data_posts = soup.select('div[data-qa^="vacancy-serp__vacancy"]')
        for post in data_posts:
            vacancy_data = get_post_data(post)
            insert_vacancy(vacancy_data)  # Вставляем данные в базу


if __name__ == '__main__':
    main()
