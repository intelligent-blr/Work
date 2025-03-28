from config import my_base, file_dir

from db_operations import (
    add_user_to_database,
    user_exists_in_database,
    fetch_user_info,
    fetch_user_email,
    add_log_search_query,
    # all_films_from_query,
    all_query_users,
    all_query_one_user,
    get_current_user_id,
    change_user_information,
    fetch_table_rows,
    find_film_year_and_genre)

from db_setup import (
    # get_connection,
    create_database,
    database_is_exists)

from search_enginee import (
    parse_stop_words,
    find_documents,
    # films_rating,
    rating_query_users)

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

    while True:
        action = input("Выберите доступное действие:\n1 - Найти фильм\n"
                       "2 - Получить статистику\n3 - Изменить свои данные\n"
                       "0 - Выход из программы.\n")

        if action == "1":
            while True:
                print("\nВарианты для поиска:\n1 - Найти фильмы по году "
                      "и жанру\n2 - Поиск фильма по ключевым словам"
                      "\n3 - Вывести статистику по самым популярным "
                      "запросам\n0 - Назад")
                choice = input("Выберите вариант поиска: ")

                if choice == "0":
                    print("Выход из режима поиска.")
                    break

                if choice == "1":
                    try:
                        input_year = input("Введите год выпуска фильма "
                                           "(если известен): ")
                        input_genre = input("Введите жанр фильма "
                                            "(если знаете): ").lower()

                        year = int(input_year) if input_year else None
                        genre = input_genre if input_genre else None

                        films = find_film_year_and_genre(year, genre)

                        if not films:
                            print("По вашему запросу ничего не найдено.")
                        else:
                            print("\nНайденные фильмы: ")

                            for _, film_title in films:
                                print(film_title)

                        found_film_ids = json.dumps(
                            [film_id for film_id, _ in films])

                        user_id = get_current_user_id(input_login)

                        user_query = f"{year}, {genre}"

                        add_log_search_query(
                            user_query, user_id, found_film_ids)

                    except ValueError:
                        print("Ошибка: Введите корректный год (целое число).")

                if choice == "2":
                    user_query = input("Введите описание фильма: ")

                    stop_words = parse_stop_words(file_dir)

                    documents = fetch_table_rows()

                    films = find_documents(documents, stop_words, user_query)

                    if isinstance(films, str):
                        print(films)
                    else:
                        films_sorted = sorted(
                            films, key=lambda x: x[1], reverse=True)

                        print("\nНайденные фильмы (id фильма, "
                              "количество совпадений):")

                        for film_id, match_count in films_sorted:
                            print(f"ID: {film_id}, совпадения: {match_count}")

                        found_film_ids = json.dumps(
                            [film[0] for film in films_sorted])

                        user_id = get_current_user_id(input_login)

                        add_log_search_query(
                            user_query, user_id, found_film_ids)

                if choice == "3":
                    queries = all_query_users()

                    rating_query_users(queries)

        if action == "2":
            while True:
                print("\nВарианты для поиска:\n1 - Ваша статистика "
                      "\n2 - Статистика по всем пользователям\n0 - Назад")
                choice = input("Выберите вариант поиска: ")

                if choice == "0":
                    print("Выход из режима поиска.")
                    break

                if choice == "1":
                    statistics_user = all_query_one_user(input_login)

                    print("\nСписок ваших запросов:")
                    print("\n".join(statistics_user))

                if choice == "2":
                    statistics_all_users = all_query_users()

                    print("\nСписок запросов всех пользователей:")
                    print("\n".join(statistics_all_users))

        elif action == "3":
            while True:
                print("\nВарианты для изменения:\n1 - Изменить login\n"
                      "2 - Изменить first_name\n3 - Изменить last_name\n"
                      "4 - Изменить email\n0 - Назад")
                field_action = input("Выберите изменение: ")

                if field_action == "0":
                    print("Выход из режима обновления данных.")
                    break

                field_map = {"1": "login", "2": "first_name",
                             "3": "last_name", "4": "email"}

                if field_action in field_map:
                    new_value = input(f"Введите новое значение для "
                                      f"{field_map[field_action]}: ")

                    change_user_information(my_base, input_login,
                                            field_map[field_action], new_value)

        elif action == "0":
            print("Выход из программы.")
            break


if __name__ == "__main__":
    main()
