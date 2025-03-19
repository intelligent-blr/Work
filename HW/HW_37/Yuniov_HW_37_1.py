import mysql.connector

# 1. В базе данных ich_edit три таблицы. Users с полями (id, name, age),
# Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).
# Программа должна запросить у пользователя название таблицы и вывести все
# ее строки или сообщение, что такой таблицы нет.

dbconfig = {'host': 'ich-edit.edu.itcareerhub.de',
            'user': 'ich1',
            'password': 'ich1_password_ilovedbs',
            'database': 'ich_edit'
            }


def fetch_table(table_name):
    tables = {'Users', 'Products', 'Sales'}

    if table_name not in tables:
        print('Такой таблицы нет')
        return

    try:
        connection = mysql.connector.connect(**dbconfig)
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {table_name}')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except mysql.connector.Error as err:
        print(f'Ошибка MySQL: {err}')
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    table_name = input("Введите название таблицы (Users, Products, Sales): ")
    fetch_table(table_name)
