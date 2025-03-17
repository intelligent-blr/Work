def validate_args(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Проверяем типы аргументов
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    print(f"Ошибка: аргумент {i + 1} должен быть типа {expected_type.__name__}, а не {type(arg).__name__}")
                    return
            # Если типы корректные, вызываем оригинальную функцию
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Пример использования декоратора

@validate_args(int, str)
def example_function(a, b):
    print(f"Аргумент 1: {a}, Аргумент 2: {b}")

# Пример с правильными типами
example_function(42, "Hello")

# Пример с неправильными типами
example_function("42", "Hello")
example_function(42, 100)