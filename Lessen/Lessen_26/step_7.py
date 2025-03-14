import argparse
import os
from typing import List

def find_files(directory: str, extension: str) -> List[str]:
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_list.append(os.path.join(root, file))
    return file_list

def merge_files(file_list: List[str], output_file: str) -> None:
    with open(output_file, "w", encoding="utf-8") as out_f:
        for file in file_list:
            try:
                with open(file, "r", encoding="utf-8") as f:
                    out_f.write(f"# === Содержимое файла: {file} ===\n")
                    out_f.write(f.read() + "\n\n")
            except Exception as e:
                print(f"Ошибка при чтении {file}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Объединение файлов определенного типа в один.")
    parser.add_argument("-d", "--directory", required=True, help="Директория для поиска файлов.")
    parser.add_argument("-e", "--extension", required=True, help="Расширение файлов (например, .txt, .log).")
    parser.add_argument("-o", "--output", default="merged.txt", help="Имя выходного файла (по умолчанию merged.txt).")

    args = parser.parse_args()

    files = find_files(args.directory, args.extension)
    
    if not files:
        print("Файлы с таким расширением не найдены!")
        return

    merge_files(files, args.output)
    print(f"Объединение завершено! Данные сохранены в '{args.output}'.")


main()


# python merge_files.py -d /путь/к/папке -e .txt
