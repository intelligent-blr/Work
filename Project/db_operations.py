from db_setup import get_connection


# def fetch_table_rows(conn, table_name: str) -> list[tuple[int, set[str]]]:
#     # таблица film и забираем film_id, title, description, release_year, special_features
#     # film_id, "title + description + special_features"
#     # [(178, set("title + description + special_features")), (179, set("title + description + special_features"))]
#     return "Список докxументов"


# def get_all_users_statistics() -> str:
#     return "Статистика по всем пользователям"


# def get_user_statistics(username: str) -> str:
#     return "Статистика по текущему пользователю"


# def change_user_information(username: str, field: str, new_value: str) -> str:
#     return "Данные пользователя изменены!"


# def user_exists_in_database(username: str) -> bool:
#     conn = get_connection(db_name='aleksei_kuritsyn_777')
#     cursor = conn.cursor()

#     query = "SELECT id FROM Users WHERE user_name = %s"
#     cursor.execute(query, (username,))
#     result = cursor.fetchone()

#     cursor.close()
#     conn.close()

#     return result is not None


# def fetch_user_info(username: str) -> dict[str, str]:
#     conn = get_connection(db_name='aleksei_kuritsyn_777')
#     cursor = conn.cursor()

#     query = "SELECT first_name, last_name FROM users WHERE user_name = %s"
#     cursor.execute(query, (username,))
#     result = cursor.fetchone()

#     cursor.close()
#     conn.close()

#     if result:
#         return {"first_name": result[0], "last_name": result[1]}
#     else:
#         raise ValueError("Пользователь не найден")


def add_user_to_database(login: str, first_name: str, # готово
                         last_name: str, email: str) -> None:
    conn = get_connection(db_name='Yuniou_300924')
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO users (login, first_name, last_name, email)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (login, first_name, last_name, email))

    conn.commit()

    cursor.close()
    conn.close()

    print(f"Пользователь {first_name} {last_name} успешно добавлен в "
          f"базу данных")


login = 'Alex_777'
first_name = 'Alex'
last_name = 'Petrov'
email = 'google@gmail.com'

if __name__ == '__main__':
    add_user_to_database(login, first_name, last_name, email)
