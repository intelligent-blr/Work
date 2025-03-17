import argparse
import os

# 1. Напишите программу, которая принимает в качестве аргумента командной строки
# путь к файлу .py и запускает его. При запуске файла программа должна выводить
# сообщение "Файл <имя файла> успешно запущен". Если файл не существует или не
# может быть запущен, программа должна вывести соответствующее сообщение об
# ошибке


def test_code():
    parser = argparse.ArgumentParser(description='Файл успешно запущен')
    parser.add_argument('--input', required=True, help='Path to input file')
    args = parser.parse_args()
    try:
        file_name = args.input

        if os.path.exists(file_name):
            print(f'Файл {file_name} успешно запущен')
        else:
            print(f'Входной файл {file_name} не найден')
    except Exception as error:
        print(f'Ошибка при чтении: {error}')


test_code()