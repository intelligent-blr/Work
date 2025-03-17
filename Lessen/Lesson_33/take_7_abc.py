from abc import ABC, abstractmethod

# Абстрактный класс
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Абстрактный метод (обязательный для всех наследников)"""
        pass

# Дочерний класс обязан реализовать make_sound
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# animal = Animal()  # ❌ Ошибка! Нельзя создать объект абстрактного класса
dog = Dog()
cat = Cat()

print(dog.make_sound())  # ✅ "Woof!"
print(cat.make_sound())  # ✅ "Meow!"
