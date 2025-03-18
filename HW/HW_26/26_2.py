import argparse

# Задача 2: Скрипт копирования/обработки файла
# Создать скрипт, который принимает:
# Обязательный аргумент — путь к входному файлу(input_file).
# Обязательный аргумент — путь к выходному файлу(output_file).
# Опциональный аргумент - -uppercase(или - u), который, если задан,
# приводит весь текст входного файла к верхнему регистру перед записью
# в выходной файл.
# python filecopy.py / path/to/source.txt / path/to/dest.txt
# Копирует содержимое source.txt в dest.txt без изменений.
# python filecopy.py / path/to/source.txt / path/to/dest.txt - -uppercase
# Читает source.txt, преобразует символы в верхний регистр, сохраняет в dest.txt


def filecopy(input_file, output_file, uppercase=False):
    try:
        with open(input_file, 'r', encoding='utf-8') as in_file:
            data = in_file.read()

        if uppercase:
            data = data.upper()

        with open(output_file, 'w', encoding='utf-8') as out_file:
            out_file.write(data)

        print(f"Файл успешно обработан и сохранен в {output_file}")
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Копирование/обработка файла")
    parser.add_argument("input_file", help="Путь к входному файлу")
    parser.add_argument("output_file", help="Путь к выходному файлу")
    parser.add_argument("-u", "--uppercase", action="store_true",
                        help="Преобразовать текст в верхний регистр")

    args = parser.parse_args()

    filecopy(args.input_file, args.output_file, args.uppercase)