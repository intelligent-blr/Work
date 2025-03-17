import logging

# 1. Напишите декоратор validate_args, который будет проверять типы аргументов
# функции и выводить сообщение об ошибке, если переданы аргументы неправильного
# типа. Декоратор должен принимать ожидаемые типы аргументов в качестве
# параметров


def validate_args(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(len(types)):
                if not isinstance(args[i], types[i]):
                    raise TypeError("Неправильный тип данных")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate_args(int, str)
def example_function(n1, n2):
    print(f"Аргумент 1: {n1}, Аргумент 2: {n2}")

example_function(11, "Hello")
# example_function("11", "Hello")
# example_function(11, 111)


# 2. Напишите декоратор log_args, который будет записывать аргументы и
# результаты вызовов функции в лог-файл. Каждый вызов функции должен быть
# записан на новой строке в формате "Аргументы: <аргументы>,
# Результат: <результат>". Используйте модуль logging для записи в лог-файл.

logging.basicConfig(filename='log.txt', level=logging.INFO, encoding='utf-8')


def log_args(func):
    def wrapper(*args, **kwargs):
        logging.info(f'Аргументы: {args}, {kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'Результат: {result}')
        return result
    return wrapper


@log_args
def add(a, b):
    return a + b


add(4, 3)