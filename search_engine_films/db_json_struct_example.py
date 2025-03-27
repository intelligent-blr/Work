# from db_setup import get_connection
import json
import random
import mysql.connector
from config import dbconfig_edit


def get_connection(db_name=None):
    conn_params = dbconfig_edit.copy()
    if db_name:
        conn_params['database'] = db_name
    return mysql.connector.connect(**conn_params)


def create_struct_database():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Создание базы данных aleksei_kuritsyn_777
        cursor.execute("DROP DATABASE IF EXISTS aleksei_kuritsyn_777")
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

        # Создание таблицы Products
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_name VARCHAR(100) NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания строки'
            )
        """)
        print("Таблица Products успешно создана")

        # Создание таблицы Cart
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Cart (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                products JSON NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Время добавления в корзину',
                FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
            )
        """)
        print("Таблица Cart успешно создана")

    except mysql.connector.Error as err:
        print(f"Ошибка MySQL: {err}")

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Соединение с MySQL закрыто")


def insert_sample_data():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("USE aleksei_kuritsyn_777")

        # Вставка данных в таблицу Users
        users = [
            ('alex_777', 'Алексей', 'Курицын'),
            ('john_doe', 'Джон', 'Доу'),
            ('maria_smith', 'Мария', 'Смит'),
            ('ivan_petrov', 'Иван', 'Петров'),
            ('olga_ivanova', 'Ольга', 'Иванова')
        ]
        cursor.executemany(
            "INSERT INTO Users (user_name, first_name, last_name) VALUES (%s, %s, %s)", users)

        # Вставка данных в таблицу Products
        products = [
            ('Ноутбук', 75000.00),
            ('Смартфон', 50000.00),
            ('Наушники', 7000.00),
            ('Клавиатура', 3000.00),
            ('Мышь', 1500.00),
            ('Монитор', 20000.00),
            ('Планшет', 45000.00),
            ('Часы', 12000.00),
            ('Телевизор', 55000.00),
            ('Колонка', 8000.00)
        ]
        cursor.executemany(
            "INSERT INTO Products (product_name, price) VALUES (%s, %s)", products)

        # Получаем ID пользователей и товаров
        cursor.execute("SELECT id FROM Users")
        user_ids = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT id FROM Products")
        product_ids = [row[0] for row in cursor.fetchall()]

        # Вставка данных в таблицу Cart (случайные товары для каждого пользователя)
        cart_entries = []
        for user_id in user_ids:
            purchased_products = random.sample(
                product_ids, random.randint(2, 5))
            cart_entries.append((user_id, json.dumps(purchased_products)))

        cursor.executemany(
            "INSERT INTO Cart (user_id, products) VALUES (%s, %s)", cart_entries)

        conn.commit()
        print("Данные успешно добавлены в таблицы")

    except mysql.connector.Error as err:
        print(f"Ошибка MySQL: {err}")

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Соединение с MySQL закрыто")


if __name__ == "__main__":
    create_struct_database()
    insert_sample_data()
