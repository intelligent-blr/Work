def split_words(text: str) -> list[str]:
    pass


def split_words_no_stop(text: str, stop_words: set[str]) -> list[str]:
    # split_words()
    pass


def parse_query(text: str, stop_words: set[str]) -> set[str]:
    words = set(text.lower().split())
    relevant_words = words.difference(stop_words)
    return relevant_words

# считаем количество вхождений слов из запроса пользователя и содержащихся в документе
def match_document(document_words: set[str], query_words: set[str]) -> int:
    return len(document_words.intersection(query_words))


def parse_stop_words(stop_words_input: str) -> set[str]:
    return set(stop_words_input.lower().split())


def find_documents(documents: list[tuple[int, set[str]]], stop_words: set[str],
                   query: str) -> list[tuple[int, int]]:
    query_no_stop_words = parse_query(query, stop_words)
    for id, document in documents:
        print(id)
        print(match_document(document, query_no_stop_words))


# documents = [(17, set({'Безумный', "Доктор", "Дэвид", "на", "горе"})),
#              (18, set({'Безумный', "Доктор", "Дэвид", "на", "горе"}))]

# find_documents(documents, '', "")
