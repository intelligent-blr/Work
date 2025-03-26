if choice == "2":  # Ключевые слова
    conn = get_connection("sakila", read_db=True)
    user_query = input("Введите описание фильма: ").strip()  # Получаем запрос пользователя
    stop_words = parse_stop_words(file_dir)  # Загружаем стоп-слова

    # Получаем строки документов
    documents = fetch_table_rows(conn)

    # Найдем совпадения по очищенному запросу
    films = find_documents(documents, stop_words, user_query)  # Передаем оригинальный запрос

    if films == "По Вашему запросу не найдено ни одного совпадения.":
        print(films)
    else:
        print("Найденные фильмы:")
        for film_id, match_count in films:
            print(f"ID фильма: {film_id}, Количество совпадений: {match_count}")
