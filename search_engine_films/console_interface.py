from db_operations import (
    get_all_users_statistics,
    add_user_to_database,
    user_exists_in_database,
    fetch_user_info,
    get_user_statistics,
    change_user_information,
    fetch_table_rows,
    database_is_exists)

from db_setup import create_struct_database, database_is_exists, get_connection

from search_enginee import (
    parse_stop_words,
    find_documents
)


def main():
    if not database_is_exists("your_database_name"):
        create_struct_database()

    username = 'alex777'
    if user_exists_in_database(username):
        user_data = fetch_user_info(username)
        print(f"Привет, {user_data['first_name']} {user_data['last_name']}!")
    else:
        first_name = "Алексей"
        last_name = "Курицын"
        add_user_to_database(username, first_name, last_name)

    action = input(
        "Выберите доступное действие: 1 - Найти фильм, 2 - Получить статистику, 3 - Изменить свои данные\n")

    if action == "1":
        # Парсинг стоп слов
        str stop_words_string = input("Введите строку стоп слов: ")
        # "быть смотреть а по с в на...".split()
        set[str] stop_words = parse_stop_words(stop_words_string)

        # Получение документов
        if conn := get_connection("sakila"):
            list[tuple[int, set[str]]] documents = fetch_table_rows(conn, table_name)
            conn.close()
        else:
            print("Не удалось подключиться к базе данных.")
    
        # Отпарвка поискового запроса
        str query = input("Введите строку запрос: ")
        for document_id, relevance in find_documents(documents, stop_words, query):
            print(
                f"Номер документа id = {document_id} | релевантность документа = {relevance}")
            # insert_data({'query': "Безумный доктер", 'response': [407, 349, 20, 398]})
    elif action == "2":
        stat_action = input(
            "1 - Статистика по всем пользователям, 2 - Статистика по вам\n")
        if stat_action == "1":
            print(get_all_users_statistics())
        elif stat_action == "2":
            print(get_user_statistics(username))
    elif action == "3":
        field_action = input(
            "Выберите действие: 1 - Сменить first_name, 2 - Сменить last_name, 3 - Сменить user_name\n")
        new_value = input("Введите новое значение: ")
        fields = {"1": "first_name", "2": "last_name", "3": "user_name"}
        if field_action in fields:
            change_user_information(username, fields[field_action], new_value)
            print("Данные успешно обновлены")
        else:
            print("Неверный ввод")


if __name__ == "__main__":
    main()
