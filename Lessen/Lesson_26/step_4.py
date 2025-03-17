import os

os.chdir('/Users/sciwake/Desktop/python_test/')
current_dir = os.getcwd()
files = os.listdir(current_dir)
os.mkdir('new_directory')
os.makedirs('new_directory/sub_directory')

for dirpath, dirnames, filenames in os.walk(current_dir):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
