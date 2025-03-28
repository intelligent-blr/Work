film_ids_list = all_films_from_query()

# Flatten the list of lists or strings (if necessary) and count the occurrences of each film ID
# If each response is a string representing a list of IDs (e.g., '[1, 2, 3]'), we need to process it into individual IDs.

# If the response is a string of comma-separated IDs:
film_ids = []
for response in film_ids_list:
    # If each response is a string of IDs, convert it into a list of integers
    response_ids = [int(id.strip()) for id in response.strip('[]').split(',')]
    film_ids.extend(response_ids)

# Now, count the occurrences of each film ID
film_counts = Counter(film_ids)

# Print the count of each film ID
for film_id, count in film_counts.items():
    print(f"Film ID: {film_id}, Count: {count}")