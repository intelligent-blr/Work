import argparse

def main():
    parser = argparse.ArgumentParser(description="Читает входной файл и записывает содержимое в выходной.")
    parser.add_argument('--input', required=True, help='Path to input file')
    parser.add_argument('--output', required=True, help='Path to output file')
    args = parser.parse_args()

    try:
        with open(args.input, 'r', encoding='utf-8') as in_file:
            data = in_file.read()
    except FileNotFoundError:
        print(f"Ошибка: входной файл '{args.input}' не найден.")
        return
    except Exception as e:
        print(f"Ошибка при чтении входного файла: {e}")
        return

    try:
        with open(args.output, 'w', encoding='utf-8') as out_file:
            out_file.write(data)
        print(f"Содержимое файла '{args.input}' успешно скопировано в '{args.output}'.")
    except Exception as e:
        print(f"Ошибка при записи в выходной файл: {e}")


main()
