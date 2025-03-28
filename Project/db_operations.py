from db_setup import get_connection

from config import my_base, table_name

from collections import Counter


# все документы формата (id, str-название+описание)
def fetch_table_rows() -> list[tuple[int, str]]:
    conn = get_connection("sakila", read_db=True)
    cursor = conn.cursor()

    query = f"""
            SELECT film_id, title, description
            FROM {table_name};
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

    cursor.close()
    conn.close()

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
        VALUES (%s, %s, %s, %s);
    """
    cursor.execute(insert_query, (login, first_name, last_name, email))
    conn.commit()

    cursor.close()
    conn.close()

    return True
    # print(f"Пользователь {first_name} {last_name} добавлен в базу данных")


# поиск существующего email
def fetch_user_email(email: str) -> dict[str, str]:
    conn = get_connection(my_base)
    cursor = conn.cursor()

    query = "SELECT email FROM users WHERE email = %s;"
    cursor.execute(query, (email,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        print("Данный email уже зарегистрирован. Пожалуйста, введите другой")
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

    query = f"UPDATE users SET {field} = %s WHERE login = %s;"
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
            SELECT
                f.film_id
                , f.title
            FROM film f
                LEFT JOIN film_category fc ON f.film_id = fc.film_id
                LEFT JOIN category c ON fc.category_id = c.category_id
            WHERE f.release_year = %s AND c.name = %s;
        """
        year_genre = (year, genre)

    elif year:
        return find_film_year(year)

    elif genre:
        return find_film_genre(genre.lower())

    else:
        return []

    cursor.execute(query, year_genre)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return [(film[0], film[1]) for film in results]


# ищем только по году
def find_film_year(year):
    conn = get_connection("sakila", read_db=True)
    cursor = conn.cursor()

    query = "SELECT film_id, title FROM film WHERE release_year = %s;"
    cursor.execute(query, [year])
    films = [(film[0], film[1]) for film in cursor.fetchall()]

    cursor.close()
    conn.close()

    return films


# ищем только по жанру
def find_film_genre(genre):
    conn = get_connection("sakila", read_db=True)
    cursor = conn.cursor()

    query = """
        SELECT
            f.film_id
            , f.title
        FROM film f
            JOIN film_category fc ON f.film_id = fc.film_id
            JOIN category c ON fc.category_id = c.category_id
        WHERE LOWER(c.name) = %s;
    """
    cursor.execute(query, [genre])
    films = [(film[0], film[1]) for film in cursor.fetchall()]

    cursor.close()
    conn.close()

    return films


# записываем данные из запроса в таблицу
def add_log_search_query(query: str, user_id: int, found_film_ids: list):
    conn = get_connection(my_base)
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO queries (query, user_id, response)
        VALUES (%s, %s, %s);
    """

    cursor.execute(insert_query, (query, user_id, found_film_ids))
    conn.commit()

    cursor.close()
    conn.close()


# поиск user_id в таблице users
def get_current_user_id(login: str):
    conn = get_connection(my_base)
    cursor = conn.cursor()

    query = "SELECT id FROM users WHERE login = %s;"
    cursor.execute(query, (login,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result[0] if result else None


# выгружаем все film_id, найденные из запросов пользователей
def all_films_from_query():
    conn = get_connection(my_base)
    cursor = conn.cursor()

    query = "SELECT response FROM queries;"

    cursor.execute(query)
    responses = cursor.fetchall()

    cursor.close()
    conn.close()

    return [response[0] for response in responses]


# выгружаем все query пользователей для статистики
def all_query_users():
    conn = get_connection(my_base)
    cursor = conn.cursor()

    queries = "SELECT query FROM queries;"

    cursor.execute(queries)
    queries = cursor.fetchall()

    cursor.close()
    conn.close()

    return [query[0] for query in queries]


# выгружаем все query одного пользователя для статистики
def all_query_one_user(input_login):
    conn = get_connection(my_base)
    cursor = conn.cursor()

    queries = """
        SELECT t1.query
            FROM queries t1
            JOIN users t2 ON t1.user_id = t2.id AND login = %s;
    """

    cursor.execute(queries, (input_login,))
    queries = cursor.fetchall()

    cursor.close()
    conn.close()

    return [query[0] for query in queries]

# queries = all_query_users()
# print(queries)
