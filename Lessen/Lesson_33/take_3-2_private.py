class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = None
        self.set_age(age)  # Используем сеттер

    def get_age(self):
        """Геттер для возраста"""
        return self.__age

    def set_age(self, age):
        """Сеттер с валидацией данных"""
        if 0 <= age <= 120:
            self.__age = age
        else:
            print("Ошибка: Возраст должен быть в диапазоне 0-120")


p = Person("Bob", 25)
print(p.get_age())  # ✅ 25

p.set_age(150)  # ❌ Ошибка: Возраст должен быть в диапазоне 0-120
print(p.get_age())  # ✅ 25 (старое значение не изменилось)
