import datetime

# 1. Реализовать класс Counter, который представляет счетчик.
# Класс должен поддерживать следующие операции:
# - Увеличение значения счетчика на заданное число (оператор +=)
# - Уменьшение значения счетчика на заданное число (оператор -=)
# - Преобразование счетчика в строку (метод __str__)
# - Получение текущего значения счетчика (метод __int__)

class Counter:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Counter(self.value + other)
        else:
            raise TypeError('Неправильный тип данных')

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Counter(self.value - other)
        else:
            raise TypeError('Неправильный тип данных')

    def __str__(self):
        return f'Counter value: {self.value}'


n = Counter(10)
print(n + 5)
print(n - 9)
print(n)

# 2. Реализовать класс Email, представляющий электронное письмо.
# Класс должен поддерживать следующие операции:
# - Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
# - Преобразование письма в строку (метод __str__)
# - Получение длины текста письма (метод __len__)
# - Получение хеш-значения письма (метод __hash__)
# - Проверка наличия текста в письме (метод __bool__)


class Email:
    def __init__(self, sender, recipient, subject, body, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = datetime.date(*map(int, date.split('-')))

    def __lt__(self, other):
        if isinstance(other, Email):
            return self.date < other.date
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Email):
            return self.date <= other.date
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Email):
            return self.date > other.date
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Email):
            return self.date >= other.date
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Email):
            return self.date == other.date
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return (f"Отправитель: {self.sender}\nАдресат: {self.recipient}\n"
               f"Тема письма: {self.subject}\nДата: {self.date}\n\n{self.body}")

    def __len__(self):
        return len(self.body)

    def __hash__(self):
        return hash((self.sender, self.recipient, self.subject, self.body, self.date))

    def __bool__(self):
        if self.body != "":
            return True
        return False


email_1 = Email("nike@google.com", "nike_1@google.com", "Кроссовки",
                "Пришлите в подарок кроссовки.", "2024-03-01")
email_2 = Email("adidas@google.com", "dadidas_1@google.com", "Подарок от Nike",
                "Nike прислал мне подарок, а Вы нет.", "2024-03-02")

print(email_1 < email_2)
print(email_1 > email_2)
print(email_1)
print(len(email_1))
print(len(email_2))

empty_email = Email("nike@google.com", "nike_1@google.com", "Подарок",
                    "", "2024-03-04")

print(bool(email_1))
print(bool(empty_email))