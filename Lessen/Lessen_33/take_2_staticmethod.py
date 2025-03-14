class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    # Метод класса для получения общего количества автомобилей
    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

    # Метод класса для создания нового объекта Car
    @classmethod
    def from_string(cls, car_str):
        brand, model = car_str.split('-')
        return cls(brand, model)

    @staticmethod
    def is_valid_car_string(car_str):
        parts = car_str.split('-')
        return len(parts) == 2 and all(parts)


# Создаем несколько объектов Car
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Общее количества автомобилей
print("Total cars:", Car.get_total_cars())  # Total cars: 2

# Новый объекта из строки
car3 = Car.from_string("Ford-Focus")
print("Car3 make:", car3.brand)  # Car3 make: Ford
print("Car3 model:", car3.model)  # Car3 model: Focus
print("Total cars:", Car.get_total_cars())  # Total cars: 3

# Используем статический метод для проверки корректности строки
print(Car.is_valid_car_string("Toyota-Camry"))  # True
print(Car.is_valid_car_string("ToyotaCamry"))  # False
