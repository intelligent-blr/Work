from db_setup import get_connection

from config import my_base, find_base

from typing import List, Tuple, Optional, Dict


# все документы формата (id, str-название+описание)
def fetch_table_rows() -> list[tuple[int, str]]:
    conn = get_connection(find_base, read_db=True)
    cursor = conn.cursor()

    query = """
            SELECT film_id, title, description
            FROM film;
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
    cursor.execute(
        insert_query, (login, first_name, last_name, email))
    conn.commit()

    cursor.close()
    conn.close()


# поиск существующего email
def fetch_user_email(email: str) -> bool:
    conn = get_connection(my_base)
    cursor = conn.cursor()

    query = "SELECT email FROM users WHERE email = %s;"
    cursor.execute(query, (email,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result is not None


# изменение информации о пользователе
def change_user_information(my_base: str, input_login: str,
                            field: str, new_value: str) -> None:
    permitted_fields = {"login", "first_name", "last_name", "email"}
    if field not in permitted_fields:
        print(f"Ошибка: изменение поля '{field}' запрещено!")
        return

    if field in {"first_name", "last_name"}:
        new_value = new_value.title()

    conn = get_connection(my_base)
    cursor = conn.cursor()

    query = f"UPDATE users SET {field} = %s WHERE login = %s;"
    cursor.execute(query, (new_value, input_login))
    conn.commit()

    cursor.close()
    conn.close()

    print(f"\nДанные по '{field}' успешно обновлены для пользователя "
          f"{new_value if field == 'login' else input_login}.")
    return True


# поиск фильмов по году и жанру
def find_film_year_and_genre(year: Optional[int],
                             genre: Optional[str]) -> List[Tuple[int, str]]:
    conn = get_connection(find_base, read_db=True)
    cursor = conn.cursor()

    if year and genre:
        query = """
            SELECT f.film_id, f.title
            FROM film f
            LEFT JOIN film_category fc ON f.film_id = fc.film_id
            LEFT JOIN category c ON fc.category_id = c.category_id
            WHERE f.release_year = %s AND c.name = %s;
        """
        cursor.execute(query, (year, genre))

    elif year:
        return find_film_year(year)

    elif genre:
        return find_film_genre(genre.lower())

    else:
        return []

    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return [(film[0], film[1]) for film in results]


# ищем только по году
def find_film_year(year: int) -> List[Tuple[int, str]]:
    conn = get_connection(find_base, read_db=True)
    cursor = conn.cursor()

    query = "SELECT film_id, title FROM film WHERE release_year = %s;"
    cursor.execute(query, [year])
    films = cursor.fetchall()

    cursor.close()
    conn.close()

    return films


# ищем только по жанру
def find_film_genre(genre: str) -> List[Tuple[int, str]]:
    conn = get_connection(find_base, read_db=True)
    cursor = conn.cursor()

    query = """
        SELECT f.film_id, f.title
        FROM film f
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c ON fc.category_id = c.category_id
        WHERE LOWER(c.name) = %s;
    """
    cursor.execute(query, [genre])
    films = cursor.fetchall()

    cursor.close()
    conn.close()

    return films


# записываем данные из запроса в таблицу
def add_log_search_query(query: str, user_id: int,
                         found_film_ids: List[int]) -> None:
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
def find_current_user_id(login: str) -> Optional[int]:
    conn = get_connection(my_base)
    cursor = conn.cursor()

    query = "SELECT id FROM users WHERE login = %s;"
    cursor.execute(query, (login,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result[0] if result else None


# выгружаем все query пользователей для статистики
def all_query_users() -> List[str]:
    conn = get_connection(my_base)
    cursor = conn.cursor()

    queries = "SELECT query FROM queries;"
    cursor.execute(queries)
    queries = cursor.fetchall()

    cursor.close()
    conn.close()

    return [query[0] for query in queries]


# выгружаем все query одного пользователя для статистики
def all_query_one_user(input_login: str) -> List[str]:
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


# выгружаем все фильмы по фамилии актера
def find_films_from_actor(last_name: str) -> List[str]:
    conn = get_connection(find_base, read_db=True)
    cursor = conn.cursor()

    query_actor = """
        SELECT f.film_id, f.title
        FROM film f
        JOIN film_actor fa ON f.film_id = fa.film_id
        JOIN actor a ON a.actor_id = fa.actor_id
        WHERE a.last_name = %s;
    """
    cursor.execute(query_actor, (last_name,))
    query_actor = cursor.fetchall()

    cursor.close()
    conn.close()

    return [(film[0], film[1]) for film in query_actor]


# выгружаем все film_id, найденные из запросов пользователей
def all_films_from_query() -> List[int]:
    conn = get_connection(my_base)
    cursor = conn.cursor()

    query = "SELECT response FROM queries;"
    cursor.execute(query)
    responses = cursor.fetchall()

    cursor.close()
    conn.close()

    return [response[0] for response in responses]


# находим фильм по film_id
def find_all_films_and_film_id() -> Dict[int, str]:
    conn = get_connection(find_base, read_db=True)
    cursor = conn.cursor()

    all_id_and_film = "SELECT film_id, title FROM film;"
    cursor.execute(all_id_and_film)
    all_id_and_film = cursor.fetchall()

    cursor.close()
    conn.close()

    return {film[0]: film[1] for film in all_id_and_film}
