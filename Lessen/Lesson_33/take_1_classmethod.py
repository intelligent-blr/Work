class MyClass:
    class_attr = "Class attribute"

    @classmethod
    def class_method(cls):
        print(cls.class_attr)


MyClass.class_method()  # Class attribute


### ПРИМЕР 1
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
    
    @classmethod
    def from_dict(cls, car_dict):
        return cls(car_dict["brand"], car_dict["model"])
    
    def __del__(self):
        Car.total_cars -= 1


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

del car3
print("Total cars:", Car.get_total_cars())  # Total cars: 2


# Используем метод класса
car_data = {"brand": "BMW", "model": "X5"}
car = Car.from_dict(car_data)

print(car.brand)  # BMW
print(car.model)  # X5
