import mysql.connector

# 2. В базе данных ich_edit три таблицы. Users с полями (id, name, age),
# Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).
# Программа должна вывести все имена из таблицы users, дать пользователю
# выбрать одно из них и вывести все покупки этого пользователя.

dbconfig = {
            'host': 'ich-edit.edu.itcareerhub.de',
            'user': 'ich1',
            'password': 'ich1_password_ilovedbs',
            'database': 'ich_edit'
            }

try:
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()

    def get_all_user_name():
        cursor.execute('SELECT name FROM Users')
        users = [user[0] for user in cursor.fetchall()]
        for user in users:
            print(user)
        return users

    def get_products(user_name):
        cursor.execute("""
                        SELECT p.prod
                        FROM Sales s
                        JOIN Product p ON s.pid = p.pid
                        JOIN Users u ON u.id = s.id
                        WHERE u.name = %s
                    """, (user_name,))
        products = cursor.fetchall()
        print(f"Покупки клиента {user_name}:")
        for product in products:
            print(product[0])

    if __name__ == "__main__":
        users = get_all_user_name()

        selected_user = input("Выберите клиента: ")
        if selected_user in users:
            get_products(selected_user)
        else:
            print("Такого клиента нет в списке")

except mysql.connector.Error as err:
    print(f'Ошибка MySQL: {err}')

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
