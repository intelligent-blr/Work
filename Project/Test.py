if choice == "1":  # Поиск по году и жанру
    try:
        input_year = input("Введите год выпуска фильма (необязательный критерий): ")
        input_genre = input("Введите жанр фильма (необязательный критерий): ").lower()

        year = int(input_year) if input_year else None
        genre = input_genre if input_genre else None

        films = find_film_year_and_genre(year, genre)

        if not films:
            print("По вашему запросу ничего не найдено.")
        else:
            print("\nНайденные фильмы:")
            for film in films:
                print(film)

        # Получаем user_id
        user_id = get_current_user_id()

        # Формируем строку запроса для логирования
        search_query = f"Год: {year}, Жанр: {genre}"

        # Логируем запрос и найденные фильмы
        found_film_ids = "; ".join(films) if films else "Нет результатов"
        add_log_search_query(search_query, user_id, found_film_ids)

    except ValueError:
        print("Ошибка: Введите корректный год (целое число).")

elif choice == "2":  # Поиск по описанию
    conn = get_connection("sakila", read_db=True)
    user_query = input("Введите описание фильма: ")
    stop_words = parse_stop_words(file_dir)

    documents = fetch_table_rows(conn)

    films = find_documents(documents, stop_words, user_query)

    if isinstance(films, str):
        print(films)
        found_film_ids = "Нет результатов"
    else:
        print("\nНайденные фильмы (ID фильма, количество совпадений):")
        for film_id, match_count in films:
            print(f"ID: {film_id}, совпадений: {match_count}")

        # Записываем только найденные ID фильмов
        found_film_ids = "; ".join(str(film[0]) for film in films) if films else "Нет результатов"

    # Закрываем соединение с БД
    conn.close()

    # Получаем user_id
    user_id = get_current_user_id()

    # Логируем запрос
    add_log_search_query(user_query, user_id, found_film_ids)
