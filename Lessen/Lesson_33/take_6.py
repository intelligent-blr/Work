# Базовый класс Appliance (прибор)
class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        print(f"{self.brand} {self.model} сейчас включён")

    def turn_off(self):
        print(f"{self.brand} {self.model} сейчас выклечен")


# Класс CoffeeMaker (кофеварка), который наследуется от Appliance
class CoffeeMaker(Appliance):
    def __init__(self, brand, model, water_tank_size):
        # Явное присваивание атрибутов базового класса
        super().__init__(brand, model)
        self.water_tank_size = water_tank_size  # Специфический атрибут для кофеварки

    def make_coffee(self):
        from time import sleep
        if self._has_water():
            print(f"{self.brand} {self.model} готовится кофе:")
            for i in range(5, 0, -1):
                print(f"Осталось {i} секунд")
                sleep(1)
            print("Кофе готов!")
        else:
            print(f"{self.brand} {self.model} необходимо добавить воды.")

    def _has_water(self):
        # Приватный метод, который проверяет наличие воды
        return self.water_tank_size > 0


my_coffee_maker = CoffeeMaker("Moulinex", "Subito", 1.5)

# Используем методы, унаследованные от базового класса
my_coffee_maker.turn_on()  
my_coffee_maker.make_coffee()  
my_coffee_maker.turn_off()  
