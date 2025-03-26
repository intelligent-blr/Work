from config import file_dir


def split_words(text: str) -> list[str]:
    pass


def split_words_no_stop(text: str, stop_words: set[str]) -> list[str]:
    # split_words()
    pass


# парсим слова введенные от пользователя - stop_words
def parse_query(text: str, stop_words: set[str]) -> set[str]:
    words = set(text.lower().split())
    relevant_words = words.difference(stop_words)
    return relevant_words


# количество вхождений слов из запроса пользователя и содержащихся в документе
def match_document(document_words: set[str], query_words: set[str]) -> int:
    return len(document_words.intersection(query_words))


# получение стоп-слов из файла
def parse_stop_words(filename: str) -> set[str]:
    with open(filename, "r", encoding="utf-8") as file:
        stop_words = file.read().strip()
    return set(stop_words.lower().split(", "))


# def find_documents(documents: list[tuple[int, set[str]]], stop_words: set[str],
#                    query: str) -> list[tuple[int, int]]:
#     query_no_stop_words = parse_query(query, stop_words)
#     for id, document in documents:
#         print(id)
#         print(match_document(document, query_no_stop_words))


# documents = [(17, set({'Безумный', "Доктор", "Дэвид", "на", "горе"})),
#              (18, set({'Безумный', "Доктор", "Дэвид", "на", "горе"}))]

# find_documents(documents, '', "")
