def find_documents(documents: list[tuple[int, str]], stop_words: list[str],
                   user_query: str) -> list[tuple[int, int]]:
    query_no_stop_words = parse_query_no_stop_words(user_query, stop_words)
    result = []
    for film_id, document in documents:
        relevance = match_document(document, query_no_stop_words)
        if relevance > 0:
            result.append((film_id, relevance))
    return result

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