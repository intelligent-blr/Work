import mysql.connector
from config import dbconfig


def create_and_populate_database():
    try:
        conn = mysql.connector.connect(
            **dbconfig
        )
        cursor = conn.cursor()

        # Создание базы данных ich_edit
        cursor.execute("CREATE DATABASE IF NOT EXISTS ich_edit")
        print("База данных ich_edit успешно создана")

        cursor.execute("USE ich_edit")

        # Создание таблицы Users
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                age INT NOT NULL
            )
        """)
        print("Таблица Users успешно создана")

        # Создание таблицы Products
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                pid INT AUTO_INCREMENT PRIMARY KEY,
                prod VARCHAR(50) NOT NULL,
                quantity INT NOT NULL
            )
        """)
        print("Таблица Products успешно создана")

        # Создание таблицы Sales
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Sales (
                sid INT AUTO_INCREMENT PRIMARY KEY,
                id INT NOT NULL,
                pid INT NOT NULL,
                FOREIGN KEY (id) REFERENCES Users(id),
                FOREIGN KEY (pid) REFERENCES Products(pid)
            )
        """)
        print("Таблица Sales успешно создана")

        # Наполнение таблицы Users данными
        users_data = [
            ('Alice', 30),
            ('Bob', 25),
            ('Charlie', 35)
        ]
        cursor.executemany("INSERT INTO Users (name, age) VALUES (%s, %s)", users_data)

        # Наполнение таблицы Products данными
        products_data = [
            ('Product1', 100),
            ('Product2', 200),
            ('Product3', 150)
        ]
        cursor.executemany("INSERT INTO Products (prod, quantity) VALUES (%s, %s)", products_data)

        # Наполнение таблицы Sales данными
        sales_data = [
            (1, 1),
            (1, 2),
            (2, 1),
            (3, 3)
        ]
        cursor.executemany("INSERT INTO Sales (id, pid) VALUES (%s, %s)", sales_data)

        conn.commit()
        print("Данные успешно добавлены в таблицы")

    except mysql.connector.Error as err:
        print(f"Ошибка MySQL: {err}")

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Соединение с MySQL закрыто")


def connect_to_mysql(db_name="ich_edit"):
    try:
        conn = mysql.connector.connect(
            **dbconfig,
            database=db_name
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Ошибка MySQL: {err}")
        return None


def fetch_user_purchases(conn):
    try:
        cursor = conn.cursor()

        # SQL запрос для получения покупок каждого пользователя
        query = """
            SELECT Users.name, Products.prod
            FROM Sales
            JOIN Users ON Sales.id = Users.id
            JOIN Products ON Sales.pid = Products.pid
            ORDER BY Users.name
        """
        cursor.execute(query)

        # Получаем результаты запроса
        purchases = cursor.fetchall()
        return purchases

    except mysql.connector.Error as err:
        print(f"Ошибка MySQL: {err}")
        return None
    finally:
        cursor.close()


def print_user_purchases(purchases):
    if purchases:
        print("Покупки каждого пользователя:")
        for name, prod in purchases:
            print(f"{name} купил {prod}")
    else:
        print("Нет данных о покупках")


def main():
    if conn := connect_to_mysql():
        if purchases := fetch_user_purchases(conn):
            print_user_purchases(purchases)
        else:
            print("Не удалось получить данные о покупках. Проверьте соединение с базой данных.")
        conn.close()
    else:
        print("Не удалось подключиться к базе данных.")


if __name__ == "__main__":
    create_and_populate_database()
    main()
