# pip install mysql-connector-python
import mysql.connector
from config import dbconfig

# Устанавливаем подключение к базе данных
connection = mysql.connector.connect(**dbconfig)
cursor = connection.cursor()

cursor.execute("SHOW DATABASES;")
print("Список баз данных:")
for (db,) in cursor:
    print(db)

cursor.fetchall()


cursor.execute("CREATE DATABASE IF NOT EXISTS test_257897;")
# cursor.fetchall()

cursor.execute("SHOW DATABASES;")
databases = [db[0] for db in cursor.fetchall()]

if 'test_257897' in databases:
    print("База данных успешно создана")

# cursor.fetchall()


cursor.execute("DROP DATABASE IF EXISTS test_257897;")
# cursor.fetchall()


cursor.execute("SHOW DATABASES;")
databases = [db[0] for db in cursor.fetchall()]

if 'test_257897' not in databases:
    print("База данных успешно удалена")

# Закрываем курсор и соединение
cursor.close()
connection.close()
