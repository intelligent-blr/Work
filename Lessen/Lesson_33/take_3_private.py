class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._mileage = 0  # Защищенный атрибут
        self.__vin = self.__generate_vin()  # Приватный атрибут

    # Приватный метод для генерации победителя
    def __generate_vin(self):
        import random
        return f"VIN{random.randint(1000, 9999)}"

    # Метод для получения защищенного атрибута
    def get_mileage(self):
        return self._mileage

    # Метод для установки защищенного атрибута
    def set_mileage(self, mileage):
        if mileage >= 0:
            self._mileage = mileage
        else:
            raise ValueError("Пробег не может быть отрицательным")

    # Метод для получения приватного атрибута
    def get_vin(self):
        return self.__vin

# Создаем объект Car
car = Car("Toyota", "Camry")

# Доступ к защищенному атрибуту через методы
car.set_mileage(5000)
print("Car mileage:", car.get_mileage())  # Car mileage: 5000

# Доступ к приватному атрибуту через метод
print("Car VIN:", car.get_vin())  # Car VIN: VINXXXX (случайное число)

# Попытка прямого доступа
# try:
print(car.brand)
car.brand = 'NeToyota'
print(car.brand)
# except AttributeError as e:
#     print("Ошибка:", e)  # Ошибка: 'Car' object has no attribute '__vin'
