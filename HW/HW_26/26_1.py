import argparse

# Задача 1: Скрипт для вывода последовательности чисел
# Написать скрипт, который принимает от пользователя следующие аргументы
# командной строки:
# Обязательный аргумент --number  (или сокращённо -n)— целое число n.
# Необязательный аргумент-флаг --reverse (или сокращённо -r), который указывает,
# что нужно вывести числа в убывающем порядке.


def main():
    parser = argparse.ArgumentParser(description="Выводим числа")
    parser.add_argument("-n", "--number", type=int,
                        required=True, help="Целое число")
    parser.add_argument("-r", "--reverse",
                        action="store_true",
                        help="Выводим числа в убывающем порядке")

    args = parser.parse_args()


    numbers = range(1, args.number + 1)
    if args.reverse:
        numbers = reversed(numbers)

    for num in numbers:
        print(num)


if __name__ == "__main__":
    main()