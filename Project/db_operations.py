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


def user_exists_in_database(login: str) -> bool:  # готово
    conn = get_connection(db_name="Yuniou_300924")
    cursor = conn.cursor()

    query = "SELECT id FROM users WHERE login = %s"
    cursor.execute(query, (login,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result is not None


def fetch_user_info(login: str) -> dict[str, str]:  # готово
    conn = get_connection(db_name="Yuniou_300924")
    cursor = conn.cursor()

    query = "SELECT first_name, last_name FROM users WHERE login = %s"
    cursor.execute(query, (login,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        print(f"Пользователь {first_name} {last_name} есть в системе")
        return {"first_name": result[0], "last_name": result[1]}

    else:
        raise ValueError("Пользователь не найден")


def add_user_to_database(login: str, first_name: str,
                         last_name: str, email: str) -> None:  # готово
    conn = get_connection(db_name="Yuniou_300924")
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


def fetch_user_email(email: str) -> dict[str, str]:  # готово
    conn = get_connection(db_name="Yuniou_300924")
    cursor = conn.cursor()

    query = "SELECT email FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        print("Этот email уже зарегистрирован. Пожалуйста, введите другой")
        return {"email": result[0]}

    else:
        raise ValueError("Email не найден")



# def get_existing_users():
#     conn = get_connection(db_name='Yuniou_300924')
#     cursor = conn.cursor()

#     cursor.execute('SELECT email FROM users')

#     users = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return {user[0] for user in users}
# print(get_existing_users())

# def email_exists(email):
#     existing_emails = get_existing_users()
#     return email in existing_emails

# while True:
#     email = input('Введите, пожалуйста, ваш почтовый ящик: ')
#     if email_exists(email):
#         print("Этот email уже зарегистрирован. Пожалуйста, введите другой.")
#     else:
#         break

# login = 'Alex_777'
# first_name = 'Alex'
# last_name = 'Petrov'
# email = 'google@gmail.com'

# if __name__ == '__main__':
    # add_user_to_database(login, first_name, last_name, email)
    # fetch_user_info('test')
    # user_exists_in_database('Alex_777')
