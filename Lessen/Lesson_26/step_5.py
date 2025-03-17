import os


path = os.path.join('/Users/sciwake/Desktop/python_test/Lesson_26', 'step_1.py')
absolute_path = os.path.abspath(path)
exists = os.path.exists(absolute_path)
is_directory = os.path.isdir(absolute_path)
is_file = os.path.isfile(absolute_path)
print(1)