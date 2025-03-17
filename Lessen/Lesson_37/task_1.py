import mysql.connector
from config import dbconfig


def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            **dbconfig,
            database="users"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Ошибка MySQL: {err}")
        return None


def fetch_users_by_age(conn, age_limit):
    try:
        cursor = conn.cursor()

        query = "SELECT * FROM users_info WHERE age > %s"
        cursor.execute(query, (age_limit,))  # Передаем age_limit как кортеж

        users = cursor.fetchall()
        return users

    except mysql.connector.Error as err:
        print(f"Ошибка MySQL: {err}")
        return -1
    finally:
        cursor.close()


def print_users(users, age_limit):
    if users:
        print(f"Пользователи старше {age_limit} лет:")
        for user in users:
            print(user)
    else:
        print(f"Нет пользователей старше {age_limit} лет")


def main():
    age_limit = int(input("Введите возраст для поиска пользователей: "))
    conn = connect_to_mysql()
    if conn:
        users = fetch_users_by_age(conn, age_limit)
        if users == -1:
            print("Не удалось получить пользователей. Проверьте соединение с базой данных.")
        print_users(users, age_limit)
        conn.close()
    else:
        print("Не удалось подключиться к базе данных.")


if __name__ == "__main__":
    main()
