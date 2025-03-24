import mysql.connector
from config import dbconfig_edit


def get_connection(db_name=None):
    conn_params = dbconfig_edit.copy()
    if db_name:
        conn_params['database'] = db_name
    return mysql.connector.connect(**conn_params)


def database_is_exists(db_name: str) -> bool:
    return True


def create_struct_database():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Создание базы данных aleksei_kuritsyn_777
        cursor.execute("CREATE DATABASE IF NOT EXISTS aleksei_kuritsyn_777")
        print("База данных aleksei_kuritsyn_777 успешно создана")

        cursor.execute("USE aleksei_kuritsyn_777")

        # Создание таблицы Users
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_name VARCHAR(50) NOT NULL,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания строки', 
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Время обновления строки'
            )
        """)
        print("Таблица Users успешно создана")

    except mysql.connector.Error as err:
        print(f"Ошибка MySQL: {err}")

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Соединение с MySQL закрыто")


if __name__ == "__main__":
    create_struct_database()
    # main()
