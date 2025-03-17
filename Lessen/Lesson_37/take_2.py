import mysql.connector
from config import dbconfig

try:
    conn = mysql.connector.connect(
        **dbconfig
    )
    cursor = conn.cursor()

    cursor.execute("DROP DATABASE IF EXISTS users")
    cursor.execute("CREATE DATABASE IF NOT EXISTS users")
    print("База данных users успешно создана")

    cursor.execute("USE users")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users_info (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL,
            age INT
        )
    """)
    print("Таблица users_info успешно создана")

    users_data = [
        ('user1', 'user1@example.com', 25),
        ('user2', 'user2@example.com', 30),
        ('user3', 'user3@example.com', 28),
        ('user4', 'user4@example.com', 29),
        ('user5', 'user5@example.com', 29)
    ]

    insert_query = "INSERT INTO users_info (username, email, age) VALUES (%s, %s, %s)"
    cursor.executemany(insert_query, users_data)
    # INSERT INTO users_info (username, email, age) VALUES ('user1', 'user1@example.com', 25);
    # INSERT INTO users_info (username, email, age) VALUES ('user2', 'user2@example.com', 30);
    # ...
    # INSERT INTO users_info (username, email, age) VALUES ('user5', 'user5@example.com', 22);

    conn.commit()

    print("Данные успешно добавлены в таблицу users_info")

except mysql.connector.Error as err:
    print(f"Ошибка MySQL: {err}")

finally:
    cursor.close()
    conn.close()
    print("Соединение с MySQL закрыто")
