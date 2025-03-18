# 1. Напишите генератор, который будет принимать на вход числа и возвращать их
# сумму. Генератор должен использовать инструкцию yield для возврата текущей
# суммы и должен продолжать принимать новые числа для добавления к сумме.
# Если генератор получает на вход число 0, он должен прекращать работу и вернуть
# окончательную сумму.


def generator_sum():
    total_sum = 0
    while True:
        number = yield total_sum
        if number == 0:
            return total_sum
        total_sum += number


summa_numbers = generator_sum()

next(summa_numbers)

while True:
    try:
        number = int(input('Число для суммирования (0 для вывода суммы): '))
        cur_summa = summa_numbers.send(number)
        print(f'Текущая сумма: {cur_summa}')
    except StopIteration as error:
        print(f"Общая сумма: {error.value}")
        break

# 2. Напишите генератор, который будет генерировать арифметическую прогрессию


def arithmetic_progression(first_number, step, count_num):
    for i in range(count_num):
        yield first_number
        first_number += step
        i += 1


first_number = int(input('Введите начальное число: '))
step = int(input('Введите шаг прогрессии: '))
count_num = int(input('Введите количество выводимых чисел: '))

for i in arithmetic_progression(first_number, step, count_num):
    print(i)