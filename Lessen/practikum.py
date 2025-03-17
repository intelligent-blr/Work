import logging

# Конфигурация логгера
logging.basicConfig(filename='function_calls.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def log_args(func):
    def wrapper(*args, **kwargs):
        # Записываем аргументы в лог
        logging.info(f'Аргументы: {args}, {kwargs}')

        # Вызов функции и получение результата
        result = func(*args, **kwargs)

        # Записываем результат в лог
        logging.info(f'Результат: {result}')

        return result
    return wrapper

# Пример использования декоратора

@log_args
def add(a, b):
    return a + b

@log_args
def greet(name):
    return f'Hello, {name}!'

# Вызовем функции для примера
add(3, 5)
greet('Alice')