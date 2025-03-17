import argparse
import os

# 2. Напишите программу, которая принимает в качестве аргумента командной строки
# путь к директории и выводит список всех файлов и поддиректорий внутри этой
# директории. Для этой задачи используйте модуль os и его функцию walk.
# Программа должна выводить полный путь к каждому файлу и директории.


def list_root_dirs_files(directory):
    for root, dirs, files in os.walk(directory):
        print(f"Root: {root}")

        for file in files:
            print(f"Files: {root}\\{file}")

        for dir in dirs:
            print(f"Dirs: {root}\\{dir}")

def main():
    parser = argparse.ArgumentParser(description="Вывести иерархию вложений")
    parser.add_argument('--directory', required=True, help="Путь к директории")
    args = parser.parse_args()

    list_root_dirs_files(args.directory)


main()