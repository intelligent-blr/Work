import random
import string

class User:
    def __init__(self, username):
        self.username = username
        self.__password = self.__generate_password()  # Приватный атрибут

    def __generate_password(self):
        """Приватный метод для создания пароля"""
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for _ in range(10))

    def get_password(self):
        """Геттер для пароля (например, если нужно показать админу)"""
        return self.__password


user1 = User("john_doe")

# print(user1.__password)  # ❌ Ошибка: приватный атрибут
print(user1.get_password())  # ✅ Показывает сгенерированный пароль
