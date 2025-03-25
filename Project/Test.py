from db_setup import get_connection
from config import my_base


def update_user_field(my_base, user_login, field, new_value):
    permitted_fields = {"login", "first_name", "last_name", "email"}
    if field not in permitted_fields:
        print(f"Ошибка: изменение поля '{field}' запрещено!")
        return

    conn = get_connection(my_base)
    cursor = conn.cursor()

    query = f"UPDATE users SET {field} = %s WHERE login = %s"
    cursor.execute(query, (new_value, user_login))

    conn.commit()
    cursor.close()
    conn.close()

    print(f"Поле '{field}' успешно обновлено для пользователя {user_login}")


def user_input_update(my_base, user_login):
    while True:
        print("\nВарианты для изменения:\n1 - login\n2 - first_name"
              "\n3 - last_name\n4 - email\n0 - Exit")

        choice = input("Введите номер: ").strip()

        if choice == "0":
            print("Выход из режима обновления данных")
            break

        field_map = {"1": "login", "2": "first_name",
                     "3": "last_name", "4": "email"}

        if choice in field_map:
            new_value = input(f"Введите новое значение для "
                              f"{field_map[choice]}: ").strip()
            update_user_field(my_base, user_login, field_map[choice], new_value)
        else:
            print("Неверный ввод, попробуйте снова")


user_login = input("Введите ваш login: ")

user_input_update(my_base, user_login)
