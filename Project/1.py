if choice == "4":
    # Шаг 1: Получаем все film_id из запросов пользователей
    query_film_ids = all_films_from_query()

    # Шаг 2: Подсчитываем количество каждого film_id
    film_id_and_count = films_rating(query_film_ids)

    # Шаг 3: Для каждого film_id выводим название фильма и количество совпадений
    for film_id, count in film_id_and_count:
        film_titles = find_films_from_film_id(film_id)

        if film_titles:  # Если фильм найден
            print(f"Название фильма: {film_titles[0]}, "
                  f"Количество совпадений: {count}")
        else:
            print(f"Фильм с ID {film_id} не найден.")
