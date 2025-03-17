from typing import List, Tuple

# 1. Напишите функцию find_longest_word, которая будет принимать список слов и
# возвращать самое длинное слово из списка. Аннотируйте типы аргументов и
# возвращаемого значения функции.


def fing_longest_word(words: List[str]) -> str:
    max_len_word = max(words, key = len)
    return max_len_word


words = ["apple", "banana", "cherry", "dragonfruit"]

result = fing_longest_word(words)

print(f"Самое длинное слово: {result}")

# 2. Напишите программу, которая будет считывать данные о продуктах из файла и
# использовать аннотации типов для аргументов и возвращаемых значений функций.
# Создайте текстовый файл "products.txt", в котором каждая строка будет содержать
# информацию о продукте в формате "название, цена, количество".

# В программе определите функцию calculate_total_price, которая будет принимать
# список продуктов и возвращать общую стоимость. Считайте данные из файла,
# разделите строки на составляющие и создайте список продуктов. Затем вызовите
# функцию calculate_total_price с этим списком и выведите результат.

with open('product.txt', 'w') as file:
    file.write("Apple, 1.50, 10\n")
    file.write("Banana, 0.75, 15\n")


def read_product(filename: str) -> List[Tuple[str, float, int]]:
    product = []
    with open(filename, 'r') as file:
        for i in file:
            name, price, quantity = i.strip().split(', ')
            name_str = str(name)
            price_float = float(price)
            quantity_int = int(quantity)
            product.append((name_str, price_float, quantity_int))
    return product


def calculate_total_price(products: List[Tuple[str, float, int]]) -> float:
    total_sum = 0
    for name, price, quantity in products:
        total_sum += price * quantity
    return total_sum


filename = 'product.txt'

products = read_product(filename)

total_sum = calculate_total_price(products)

print(f'Общая стоимость продуктов: {total_sum}')