import argparse
import collections
from typing import List, Tuple

def analyze_text(file_path: str, top_n: int) -> None:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines: List[str] = file.readlines()
            text: str = " ".join(lines)

            num_lines: int = len(lines)
            words: List[str] = text.split()
            num_words: int = len(words)
            num_chars: int = len(text)

            word_counts: collections.Counter = collections.Counter(words)
            most_common_words: List[Tuple[str, int]] = word_counts.most_common(top_n)

            print(f"Строк: {num_lines}")
            print(f"Слов: {num_words}")
            print(f"Символов: {num_chars}")
            
            print("Топ самых частых слов:")
            for i, (word, count) in enumerate(most_common_words, 1):
                print(f"{i}. \"{word}\" ({count} раз)")

    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")


parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Анализатор текста в файле.")
parser.add_argument("-f", "--file", required=True, help="Путь к текстовому файлу.")
parser.add_argument("-m", "--most_common", type=int, default=1, help="Количество самых частых слов для вывода (по умолчанию 1).")

args: argparse.Namespace = parser.parse_args()
analyze_text(args.file, args.most_common)
