from config import my_base, file_dir

from db_operations import (
    add_user_to_database,
    user_exists_in_database,
    fetch_user_info,
    fetch_user_email,
    # get_all_users_statistics,
    # get_user_statistics,
    change_user_information,
    fetch_table_rows)

from db_setup import create_database, database_is_exists, get_connection

from search_enginee import parse_stop_words, find_documents


def main():
    if not database_is_exists(my_base):
        create_database()

    input_login = input("Для входа в систему введите Ваш логин: ")
    if user_exists_in_database(input_login):
        login_data = fetch_user_info(input_login)
        print(f"Добро пожаловать {login_data['first_name']} "
              f"{login_data['last_name']}!")
    else:
        first_name = input("Необходимо выполнить регистрацию. "
                           "Введите, пожалуйста, Ваше имя: ")
        last_name = input("Введите Вашу фамилию: ")

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
                print("Выход из режима поиска")
                break

            year = int(input("Введите год выпуска фильма: "))
            feature = input("Введите special_features: ").strip()

            films = find_release_year_and_special_features(year, feature)

            if isinstance(films, str):
                    print(films)
            else:
                for film in films:
                        print(film)

            if conn := get_connection("sakila", read_db=True):
                documents = fetch_table_rows(conn)
                conn.close()
            else:
                print("Не удалось подключиться к базе данных.")
                return

        # query = input("Введите строку запроса: ")
        # for document_id, relevance in find_documents(documents, stop_words, query):
        #     print(
        #         f"Номер документа id = {document_id} | релевантность документа = {relevance}")
    # elif action == "2":
    #     stat_action = input(
    #         "1 - Статистика по всем пользователям, 2 - Статистика по вам\n")
    #     if stat_action == "1":
    #         print(get_all_users_statistics())
    #     elif stat_action == "2":
    #         print(get_user_statistics(login))
    elif action == "3":
        while True:
            print("\nВарианты для изменения:\n1 - Изменить login\n"
                  "2 - Изменить first_name\n3 - Изменить last_name\n"
                  "4 - Изменить email\n0 - Exit")
            field_action = input("Выберите изменение: ")

            if field_action == "0":
                print("Выход из режима обновления данных")
                break

            field_map = {"1": "login", "2": "first_name",
                         "3": "last_name", "4": "email"}

            if field_action in field_map:
                new_value = input(f"Введите новое значение для "
                                  f"{field_map[field_action]}: ")

                change_user_information(my_base, input_login,
                                        field_map[field_action], new_value)
            else:
                print("Неверный ввод, попробуйте снова")
    #     else:
    #         print("Неверный ввод")


if __name__ == "__main__":
    main()
