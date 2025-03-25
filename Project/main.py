from config import my_base

from db_operations import (
    # get_all_users_statistics,
    add_user_to_database,
    user_exists_in_database,
    fetch_user_info,
    fetch_user_email,
    # get_user_statistics,
    # change_user_information,
    fetch_table_rows)

from db_setup import create_database, database_is_exists, get_connection

from search_enginee import (
    parse_stop_words,
    find_documents
)


def main():
    if not database_is_exists(my_base):
        create_database()

    input_login = input("Для входа в систему введите Ваш логин: ")
    if user_exists_in_database(input_login):
        login_data = fetch_user_info(input_login)
        print(f"Рады Вас снова видеть {login_data['first_name']} "
              f"{login_data['last_name']}!")
    else:
        first_name = input("Введите, пожалуйста, Ваше имя: ")
        last_name = input("Введите, пожалуйста, Вашу фамилию: ")

        while True:
            email = input("Введите, пожалуйста, Ваш почтовый ящик: ")
            try:
                fetch_user_email(email)
                print("Этот email уже существует")
                choice = input(
                    "Хотите ввести другой email? (да/нет): ").strip().lower()
                if choice != "да":
                    print("К сожалению, вы не зарегистрированы")
                    return
            except ValueError:
                break

        add_user_to_database(input_login, first_name, last_name, email)
        print("Вы успешно зарегистрированы!")

    action = input("Выберите доступное действие:\n1 - Найти фильм\n"
                   "2 - Получить статистику\n3 - Изменить свои данные\n")

    if action == "1":
        stop_words_input = input("Введите строку стоп слов: ")
        stop_words = parse_stop_words(stop_words_input)

        # Получение документов
        if conn := get_connection("sakila"):
            documents = fetch_table_rows(conn, "film")
            conn.close()
        else:
            print("Не удалось подключиться к базе данных.")
            return

        # Отпарвка поискового запроса
        query = input("Введите строку запроса: ")
        for document_id, relevance in find_documents(documents, stop_words, query):
            print(
                f"Номер документа id = {document_id} | релевантность документа = {relevance}")

    elif action == "2":
        # Логика для получения статистики
        print("Получаем статистику...")
    elif action == "3":
        # Логика для изменения данных пользователя
        print("Изменяем ваши данные...")
    else:
        print("Неверный выбор действия.")

        # insert_data({'query': "Безумный доктер", 'response': [407, 349, 20, 398]})

    # elif action == "2":
    #     stat_action = input(
    #         "1 - Статистика по всем пользователям, 2 - Статистика по вам\n")
    #     if stat_action == "1":
    #         print(get_all_users_statistics())
    #     elif stat_action == "2":
    #         print(get_user_statistics(login))
    # elif action == "3":
    #     field_action = input(
    #         "Выберите действие: 1 - Сменить first_name, 2 - Сменить last_name, 3 - Сменить user_name\n")
    #     new_value = input("Введите новое значение: ")
    #     fields = {"1": "first_name", "2": "last_name", "3": "user_name"}
    #     if field_action in fields:
    #         change_user_information(login, fields[field_action], new_value)
    #         print("Данные успешно обновлены")
    #     else:
    #         print("Неверный ввод")


if __name__ == "__main__":
    main()
