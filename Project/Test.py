def add_log_search_query(query: str, user_id: int, response: list):
    conn = get_connection(my_base)
    cursor = conn.cursor()

    response_str = "; ".join(response) if response else "Нет результатов"

    insert_query = """
        INSERT INTO queries (query, user_id, response)
        VALUES (%s, %s, %s);
    """
    print(f"Executing query: {insert_query}") # убрать - для отладки
    print(f"user_id = {user_id}") # убрать - для отладки
    cursor.execute(insert_query, (query, user_id, response_str))
    conn.commit()

    cursor.close()
    conn.close()

    def get_current_user_id(login: str):
    conn = get_connection(my_base)
    cursor = conn.cursor()

    query = "SELECT id FROM users WHERE login = %s;"
    cursor.execute(query, (login,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result[0] if result else None

from config import my_base, file_dir

from db_operations import (
    add_user_to_database,
    user_exists_in_database,
    fetch_user_info,
    fetch_user_email,
    # get_all_users_statistics,
    # get_user_statistics,
    add_log_search_query,
    get_current_user_id,
    change_user_information,
    fetch_table_rows,
    find_film_year_and_genre)

from db_setup import (
    get_connection,
    create_database,
    database_is_exists)

from search_enginee import parse_stop_words, find_documents, parse_query

import json


def main():
    if not database_is_exists(my_base):
        create_database()

    input_login = input("Для входа в систему введите ваш логин: ")
    if user_exists_in_database(input_login):
        login_data = fetch_user_info(input_login)
        print(f"Добро пожаловать {login_data['first_name']} "
              f"{login_data['last_name']}!")
    else:
        first_name = input("Необходимо выполнить регистрацию. "
                           "Введите, пожалуйста, ваше имя: ")
        last_name = input("Введите вашу фамилию: ")

        while True:
            email = input("Последним шагом необходимо ввести email: ")
            try:
                fetch_user_email(email)
                choice = input(
                    "Хотите ввести другой email? (да/нет): ").lower()
                if choice != "да":
                    print("К сожалению, вы не выполнили регистрацию")
                    return
            except ValueError:
                break

        add_user_to_database(input_login, first_name, last_name, email)
        print(f"Регистрация прошла успешно! Добро пожаловать "
              f"{first_name} {last_name}!")

    action = input("Выберите доступное действие:\n1 - Найти фильм\n"
                   "2 - Получить статистику\n3 - Изменить свои данные\n")

    if action == "1":
        while True:
            print("\nВарианты для поиска:\n1 - Найти фильмы по году и жанру\n"
                  "2 - Ввести описание фильма\n3 - Вывести статистику по "
                  "самым популярным запросам\n0 - Exit")
            choice = input("Выберите вариант поиска: ")

            if choice == "0":
                print("Выход из режима поиска.")
                break

            if choice == "1":  # год и жанр
                try:
                    input_year = input("Введите год выпуска фильма "
                                       "(необязательный критерий): ")
                    input_genre = input("Введите жанр фильма "
                                        "(необязательный критерий): ").lower()

                    year = int(input_year) if input_year else None
                    genre = input_genre if input_genre else None

                    films = find_film_year_and_genre(year, genre)

                    if not films:
                        print("По вашему запросу ничего не найдено.")
                    else:
                        print("\nНайденные фильмы: ")
                        for film in films:
                            print(film)

                    # user_id = get_current_user_id(input_login)
                    # search_query = f"{year}, {genre}"
                    # found_film_id = ", ".join(films) if films else "Нет результатов"
                    # add_log_search_query(search_query, user_id, found_film_id)

                except ValueError:
                    print("Ошибка: Введите корректный год (целое число).")

            if choice == "2":  # ключевые слова
                conn = get_connection("sakila", read_db=True)
                user_query = input("Введите описание фильма: ")
                stop_words = parse_stop_words(file_dir)

                documents = fetch_table_rows(conn)

                films = find_documents(documents, stop_words, user_query)

                if isinstance(films, str):
                    print(films)
                else:
                    print("\nНайденные фильмы (id фильма, "
                          "количество совпадений):")
                    for film_id, match_count in films:
                        print(f"ID: {film_id}, совпадений: {match_count}")

                    found_film_ids = []
                    found_film_ids = json.dumps([film[0] for film in films]

                    print(f"DEBUG JSON перед записью: {found_film_ids}")  # Проверка

                    user_id = get_current_user_id(input_login)
                    search_query = user_query
                    add_log_search_query(search_query, user_id, found_film_ids)