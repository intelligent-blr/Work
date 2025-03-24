import mysql.connector
from config import dbconfig_edit, dbconfig_read


def get_connection(db_name=None, read_db=False):
    try:
        conn_params = dbconfig_read.copy() if read_db else dbconfig_edit.copy()
        if db_name:
            conn_params['database'] = db_name
        print(f"Подключение к базе данных: {conn_params.get('database', 'ich')}")
        return mysql.connector.connect(**conn_params)

    except mysql.connector.Error as err:
        print(f"Ошибка подключения к базе данных: {err}")
        return None

#######################################################
# conn = get_connection()
# conn = get_connection(read_db=True)
# cursor = conn.cursor()
# cursor.close()
# conn.close()
########################################################

# def database_is_exists(db_name, read_db=False):
#     try:
#         conn_params = dbconfig_read.copy() if read_db else dbconfig_edit.copy()

#         conn_params.pop(None)
#         connection = mysql.connector.connect(**conn_params)

#         if connection.is_connected():
#             print("Подключение успешно!")

#             cursor = connection.cursor()
#             cursor.execute("SHOW DATABASES;")

#             databases = [db[0] for db in cursor.fetchall()]
#             if db_name in databases:
#                 print(f"База данных '{db_name}' существует")
#                 return True
#             else:
#                 print(f"База данных '{db_name}' не найдена")
#                 return False

#         else:
#             print("Не удалось подключиться к серверу MySQL")
#             return False

#     except mysql.connector.Error as err:
#         print(f"Ошибка подключения к базе данных: {err}")
#         return False

#     finally:
#         # Закрываем соединение и курсор
#         if connection and connection.is_connected():
#             cursor.close()
#             connection.close()

# # Пример использования
# db_name = "ich"
# exists = database_is_exists(db_name, read_db=True)
# if exists:
#     print(f"База данных '{db_name}' доступна для использования.")
# else:
#     print(f"База данных '{db_name}' не существует.")




# def create_database():
#     try:
#         connection_edit = get_connection_edit()
#         cursor = connection_edit.cursor()
#         cursor.execute("CREATE DATABASE IF NOT EXISTS Yuniou_300924;")
#         print("База данных Yuniou_300924 успешно создана")
#     except mysql.connector.Error as err:
#         print(f"Ошибка: {err}")
#     finally:
#         cursor.close()
#         connection_edit.close()


# def create_tables():
#     connection_edit = get_connection_edit()
#     cursor = connection_edit.cursor()
#     cursor.execute("USE Yuniou_300924")
#     print('Подключился')
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             login VARCHAR(20) NOT NULL UNIQUE CHECK (CHAR_LENGTH(login) >= 5),
#             first_name VARCHAR(30) NOT NULL,
#             last_name VARCHAR(30) NOT NULL,
#             email VARCHAR(30) NOT NULL UNIQUE,
#             creation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
#             update_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
#         )
#     """)
#     print("Таблица users успешно создана")


# def insert_users(login, first_name, last_name, email):
#     connection_edit = get_connection_edit()
#     cursor = connection_edit.cursor()
#     cursor.execute("USE Yuniou_300924")
#     insert_query = """
#         INSERT INTO users (login, first_name, last_name, email)
#         VALUES (%s, %s, %s, %s)
#     """

#     try:
#         cursor.execute(insert_query, (login, first_name, last_name, email))
#         connection_edit.commit()
#         print("Пользователь успешно добавлен")
#     except mysql.connector.Error as err:
#         print(f"Ошибка: {err}")
#     finally:
#         cursor.close()
#         connection_edit.close()


# create_tables()

# login = 'Alex_777'
# first_name = 'Alex'
# last_name = 'Petrov'
# email = 'google@gmail.com'

# insert_users(login, first_name, last_name, email)
# # if __name__ == '__main__':
# #     create_database()
# #     create_tables()
