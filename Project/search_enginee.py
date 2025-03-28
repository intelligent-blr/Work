from collections import Counter

# парсим слова введенные от пользователя - stop_words
def parse_query_no_stop_words(user_query: str,
                              stop_words: set[str]) -> set[str]:
    user_query = set(user_query.lower().split())
    relevant_words = user_query.difference(stop_words)
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
def find_documents(documents: list[tuple[int, str]], stop_words: list[str],
                   user_query: str) -> list[tuple[int, int]]:
    query_no_stop_words = parse_query_no_stop_words(user_query, stop_words)
    result = []

    for film_id, document in documents:
        relevance = match_document(document, query_no_stop_words)
        if relevance > 0:
            result.append((film_id, relevance))
    return result


# преобразуем данные и считаем количество одинаковых film_id, сортируем
def films_rating(query_film_ids):
    film_ids = []
    for response in list:
        response_ids = [int(id) for id in response.strip('[]').split(', ')]
        film_ids.extend(response_ids)

    film_counts = Counter(film_ids)
    sorted_film_counts = film_counts.most_common()

    for film_id, count in sorted_film_counts:
        print(f"ID фильма: {film_id}, Количество совпадений: {count}")


# считаем повторения в запросах пользователей
def rating_query_users(queries):
    query_counts = Counter(queries)

    for query, count in query_counts.items():
        print(f"Запрос: {query}, Повторения: {count}")
