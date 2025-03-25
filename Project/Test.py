def fetch_table_rows(conn, table_name: str) -> list[tuple[int, set[str]]]:
    query = """
            SELECT film_id, title, description, release_year, special_features
            FROM film
            """

    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        film_id = row[0]
        combined_text = " ".join([str(row[1]), str(row[2]), str(row[4])])
        word_set = set(combined_text.split())
        result.append((film_id, word_set))
    print(result)
    return result

    if action == "1":
        stop_words = input("Введите строку стоп слов: ")

        stop_words = parse_stop_words(stop_words)

        # Получение документов
        if conn := get_connection("sakila"):

            documents = fetch_table_rows(conn, "film")
            conn.close()
        else:
            print("Не удалось подключиться к базе данных.")

        # Отпарвка поискового запроса
        query = input("Введите строку запроса: ")
        for document_id, relevance in find_documents(documents, stop_words, query):
            print(
                f"Номер документа id = {document_id} | релевантность документа = {relevance}")
            insert_data({'query': "Безумный доктер", 'response': [407, 349, 20, 398]})


def parse_query(text: str, stop_words: set[str]) -> set[str]: