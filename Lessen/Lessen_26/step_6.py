import os

def process_directory(directory: str) -> None:
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            print(file_path)
        elif os.path.isdir(file_path):
            process_directory(file_path)

start_directory = '/Users/sciwake/Desktop/python_test/search_engine/'
process_directory(start_directory)
