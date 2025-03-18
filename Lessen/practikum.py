def sum_generator():
    total = 0
    while True:
        number = yield total  # Возвращает текущую сумму и получает новое число
        if number == 0:
            return total  # Завершает работу при вводе 0
        total += number

# Использование генератора для пошагового расчета суммы
print("Введите числа для суммирования (0 для окончания):")
sum_gen = sum_generator()
next(sum_gen)  # Запуск генератора

while True:
    try:
        num = int(input("Введите число: "))
        current_sum = sum_gen.send(num)
        print(f"Текущая сумма: {current_sum}")
        if num == 0:
            break
    except StopIteration as e:
        print(f"Окончательная сумма: {e.value}")
        break
