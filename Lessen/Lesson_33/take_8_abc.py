from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        """Метод, который обязаны реализовать все фигуры"""
        pass

class Circle(Drawable):
    def draw(self):
        print("Рисуем круг")

class Square(Drawable):
    def draw(self):
        print("Рисуем квадрат")

# Используем интерфейсный подход
shapes = [Circle(), Square()]
for shape in shapes:
    shape.draw()
