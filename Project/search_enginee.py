from config import file_dir
from db_operations import fetch_table_rows
from db_setup import get_connection


# парсим слова введенные от пользователя - stop_words
def parse_query(query: str, stop_words: set[str]) -> set[str]:
    query = set(query.lower().split())
    relevant_words = query.difference(stop_words)
    return relevant_words


# количество вхождений слов из запроса пользователя и содержащихся в документе
def match_document(document_words: set[str], query_words: set[str]) -> int:
    return len(document_words.intersection(query_words))


# получение стоп-слов из файла
def parse_stop_words(filename: str) -> set[str]:
    with open(filename, "r", encoding="utf-8") as file:
        stop_words = file.read().strip()
    return set(stop_words.lower().split(", "))


# находим фильмы - -стоп слова и выводим с количеством совпадений
def find_documents(documents, stop_words: set[str],
                   query: str) -> list[tuple[int, int]]:
    query_no_stop_words = parse_query(query, stop_words)
    result = []
    for film_id, document in documents:
        relevance = match_document(document, query_no_stop_words)
        if relevance > 0:
            result.append((film_id, relevance))
            print(f"film_id: {film_id}, match_count: {relevance}")

    if not result:
        return "По Вашему запросу не найдено ни одного совпадения"

    return result


query = "zorro"
conn = get_connection("sakila", read_db=True)
documents = fetch_table_rows(conn)
stop_words = parse_stop_words(file_dir)
results = find_documents(documents, stop_words, query)
print(results)
