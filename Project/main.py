from db_operations import (
    get_all_users_statistics,
    add_user_to_database,
    user_exists_in_database,
    fetch_user_info,
    fetch_user_email,
    get_user_statistics,
    change_user_information,
    fetch_table_rows,
    database_is_exists)

from db_setup import create_database, database_is_exists, get_connection

from search_enginee import (
    parse_stop_words,
    find_documents
)


def main():
    if not database_is_exists("Yuniou_300924"):
        create_database()

    login = "Alex_777"
    if user_exists_in_database(login):
        login_data = fetch_user_info(login)
        print(f"Рады Вас снова видеть {login_data['first_name']} "
              f"{login_data['last_name']}!")
    else:
        first_name = input("Введите, пожалуйста, Ваше имя: ")
        last_name = input("Введите, пожалуйста, Вашу фамилию: ")
        email = input("Введите, пожалуйста, Ваш почтовый ящик: ")

        try:
            fetch_user_email(email)
            print("Этот email уже зарегистрирован. Пожалуйста, введите другой")
        except ValueError:
            add_user_to_database(login, first_name, last_name, email)
            print("Вы успешно зарегистрированы!")

    # action = input(
    #     "Выберите доступное действие: 1 - Найти фильм, 2 - Получить статистику, 3 - Изменить свои данные\n")

    # if action == "1":
    #     # Парсинг стоп слов
    #     str stop_words_string = input("Введите строку стоп слов: ")
    #     # "быть смотреть а по с в на...".split()
    #     set[str] stop_words = parse_stop_words(stop_words_string)

    #     # Получение документов
    #     if conn := get_connection("sakila"):
    #         list[tuple[int, set[str]]] documents = fetch_table_rows(conn, table_name)
    #         conn.close()
    #     else:
    #         print("Не удалось подключиться к базе данных.")

    #     # Отпарвка поискового запроса
    #     str query = input("Введите строку запрос: ")
    #     for document_id, relevance in find_documents(documents, stop_words, query):
    #         print(
    #             f"Номер документа id = {document_id} | релевантность документа = {relevance}")
    #         # insert_data({'query': "Безумный доктер", 'response': [407, 349, 20, 398]})
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
