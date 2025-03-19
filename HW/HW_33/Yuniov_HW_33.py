from abc import ABC, abstractmethod
import math

# 1. Реализуйте класс Employee, представляющий сотрудника компании.
# Класс должен иметь статическое поле company с названием компании,
# а также методы: set_company(cls, name): метод класса для изменения
# названия компании __init__(self, name, position): конструктор,
# принимающий имя и должность сотрудника get_info(self): метод,
# возвращающий информацию о сотруднике в виде строки
# (имя, должность, название компании)


class Employee:
    company = "ABC"

    @classmethod
    def set_company(cls, name):
        cls.company = name

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"""
                Name: {self.name}
                Position: {self.position}
                Company: {self.company}
                """


employee1 = Employee("Alex", "Director")
employee2 = Employee("Alice", "HR")

print(employee1.get_info())

Employee.set_company("BCA")

print(employee2.get_info())

# 2. Реализуйте абстрактный базовый класс Shape (фигура), а от него
# унаследуйте классы Rectangle (прямоугольник) и Circle (круг).
# Класс Shape должен иметь абстрактный метод area, который должен
# быть реализован в каждом дочернем классе. Классы Rectangle и Circle
# также должны иметь метод perimeter для расчета периметра.
# Выведите площадь и периметр прямоугольника и круга на экран.


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


rectangle = Rectangle(10, 5)
circle = Circle(5)

print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")
