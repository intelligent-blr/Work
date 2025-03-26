from db_setup import get_connection

from config import my_base


def fetch_table_rows(conn, table_name: str) -> list[tuple[int, set[str]]]:
    query = """
            SELECT film_id, title, description, release_year, special_features
            FROM film
            """

    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:
        print("По Вашему запросу ничего не найдено")
        return []

    result = []
    for row in rows:
        film_id = row[0]
        release_year = row[3]
        combined_text = " ".join([str(row[1]), str(row[2]), str(row[4])])
        word_set = set(combined_text.split())
        result.append((film_id, word_set, release_year))
    return result


result = fetch_table_rows(get_connection("sakila"), "film")
print("Найдено", result)


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


# поиск имени в фамилии в базе при существующем login
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
        raise ValueError("Пользователь не найден")


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
    print(f"Поле '{field}' успешно обновлено для пользователя {input_login}")
