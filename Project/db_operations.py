from db_setup import get_connection

from config import my_base, table_name


# все документы формата (id, str-название+описание)
def fetch_table_rows(conn) -> list[tuple[int, str]]:
    cursor = conn.cursor()

    query = f"""
            SELECT film_id, title, description
            FROM {table_name}
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:
        print("По Вашему запросу ничего не найдено.")
        return []

    documents = [
        (film_id, set(f"{title} {description}".lower().split()))
        for film_id, title, description in rows
    ]

    return documents


# conn = get_connection("sakila", read_db=True)
# result = fetch_table_rows(conn)
# print(result)


# def get_all_users_statistics() -> str:
#     return "Статистика по всем пользователям"


# def get_user_statistics(username: str) -> str:
#     return "Статистика по текущему пользователю"

# проверка существования login в системе
def user_exists_in_database(input_login: str) -> bool:
    conn = get_connection(my_base)
    cursor = conn.cursor()

    query = "SELECT id FROM users WHERE login = %s"
    cursor.execute(query, (input_login,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result is not None


# поиск имени и фамилии в базе при существующем login
def fetch_user_info(input_login: str) -> dict[str, str]:
    conn = get_connection(my_base)
    cursor = conn.cursor()

    query = "SELECT first_name, last_name FROM users WHERE login = %s"
    cursor.execute(query, (input_login,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return {"first_name": result[0], "last_name": result[1]}
    else:
        raise ValueError("Пользователь не найден.")


# добавление нового пользователя
def add_user_to_database(login: str, first_name: str,
                         last_name: str, email: str) -> None:
    conn = get_connection(my_base)
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO users (login, first_name, last_name, email)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (login, first_name, last_name, email))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Пользователь {first_name} {last_name} добавлен в базу данных")


# поиск существующего email
def fetch_user_email(email: str) -> dict[str, str]:
    conn = get_connection(my_base)
    cursor = conn.cursor()

    query = "SELECT email FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        print("Данный email уже зарегистрирован. Пожалуйста, введите другой")
        return {"email": result[0]}
    else:
        raise ValueError("Email не найден")


# изменение информации о пользователе
def change_user_information(my_base: str, input_login: str,
                            field: str, new_value: str) -> str:
    permitted_fields = {"login", "first_name", "last_name", "email"}
    if field not in permitted_fields:
        print(f"Ошибка: изменение поля '{field}' запрещено!")
        return

    conn = get_connection(my_base)
    cursor = conn.cursor()

    query = f"UPDATE users SET {field} = %s WHERE login = %s"
    cursor.execute(query, (new_value, input_login))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Поле '{field}' успешно обновлено для пользователя {input_login}.")


# поиск фильмов по году и жанру
def find_film_year_and_genre(year: int, genre: str):
    conn = get_connection("sakila", read_db=True)
    cursor = conn.cursor()

    if year and genre:
        query = """
            SELECT f.title
            FROM film f
                LEFT JOIN film_category fc ON f.film_id = fc.film_id
                LEFT JOIN category c ON fc.category_id = c.category_id
            WHERE f.release_year = %s AND c.name = %s;
        """
        params = (year, genre)

    elif year:
        return find_film_year(year)

    elif genre:
        return find_film_genre(genre.lower())

    else:
        return []

    cursor.execute(query, (params))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return [film[0] for film in results]


# ищем только по году
def find_film_year(year):
    conn = get_connection("sakila", read_db=True)
    cursor = conn.cursor()

    query = "SELECT title FROM film WHERE release_year = %s"
    cursor.execute(query, [year])
    films = [row[0] for row in cursor.fetchall()]

    cursor.close()
    conn.close()
    return films


# ищем только по жанру
def find_film_genre(genre):
    conn = get_connection("sakila", read_db=True)
    cursor = conn.cursor()

    query = """
        SELECT title FROM film f
            JOIN film_category fc ON f.film_id = fc.film_id
            JOIN category c ON fc.category_id = c.category_id
        WHERE LOWER(c.name) = %s
    """
    cursor.execute(query, [genre])
    films = [row[0] for row in cursor.fetchall()]

    cursor.close()
    conn.close()
    return films

# films = find_film_year_and_genre(2012, "Drama")

# if films:
#     print("Найденные фильмы:")
#     for film in films:
#         print(film)
# else:
#     print("По Вашему запросу ничего не найдено.")
