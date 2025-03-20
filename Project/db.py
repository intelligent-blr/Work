import mysql.connector
from config import dbconfig_edit, dbconfig_read


def get_connection_edit():
    connection_edit = mysql.connector.connect(**dbconfig_edit)
    return connection_edit


def get_connection_read():
    connection_read = mysql.connector.connect(**dbconfig_read)
    return connection_read


def create_database():
    try:
        connection_edit = get_connection_edit()
        cursor = connection_edit.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS Yuniou_300924;")
        print("База данных Yuniou_300924 успешно создана")
    except mysql.connector.Error as err:
        print(f"Ошибка: {err}")
    finally:
        cursor.close()
        connection_edit.close()


def create_tables():
    connection_edit = get_connection_edit()
    cursor = connection_edit.cursor()
    cursor.execute("USE Yuniou_300924")
    print('Подключился')
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            login VARCHAR(20) NOT NULL UNIQUE CHECK (CHAR_LENGTH(login) >= 5),
            first_name VARCHAR(30) NOT NULL,
            last_name VARCHAR(30) NOT NULL,
            email VARCHAR(30) NOT NULL UNIQUE,
            creation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            update_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
    """)
    print("Таблица users успешно создана")


def insert_users(login, first_name, last_name, email):
    connection_edit = get_connection_edit()
    cursor = connection_edit.cursor()
    cursor.execute("USE Yuniou_300924")
    insert_query = """
        INSERT INTO users (login, first_name, last_name, email)
        VALUES (%s, %s, %s, %s)
    """

    try:
        cursor.execute(insert_query, (login, first_name, last_name, email))
        connection_edit.commit()
        print("Пользователь успешно добавлен")
    except mysql.connector.Error as err:
        print(f"Ошибка: {err}")
    finally:
        cursor.close()
        connection_edit.close()


create_tables()

login = 'Alex_777'
first_name = 'Alex'
last_name = 'Petrov'
email = 'google@gmail.com'

insert_users(login, first_name, last_name, email)
# if __name__ == '__main__':
#     create_database()
#     create_tables()
