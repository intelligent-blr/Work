from config import file_dir

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

from search_enginee import parse_stop_words, find_documents, parse_query, match_document



def find_documents(conn, stop_words: set[str], query: str) -> list[tuple[int, int]]:
    query_no_stop_words = parse_query(query, stop_words)  # Очищаем запрос от стоп-слов
    documents = fetch_table_rows(conn)  # Получаем документы из базы данных
    result = []

    for film_id, document in documents:
        match_count = match_document(document, query_no_stop_words)  # Считаем количество совпадений
        if match_count > 0:
            result.append((film_id, match_count))

    return result


# Основной код
def main():
    query = "zorro"  # Запрос пользователя

    # Получаем соединение с базой данных
    conn = get_connection("sakila", read_db=True)

    # Загружаем стоп-слова только один раз
    stop_words = parse_stop_words(file_dir)

    # Находим документы, соответствующие запросу
    results = find_documents(conn, stop_words, query)

    # Выводим результаты поиска
    if results:
        print("Результаты поиска:")
        for film_id, match_count in results:
            print(f"Document ID: {film_id}, Match Count: {match_count}")
    else:
        print("Не найдено совпадений для запроса.")

# Запуск программы
if __name__ == "__main__":
    main()
