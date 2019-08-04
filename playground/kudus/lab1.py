import os


def print_file(path):
    with open(path) as f:
        for line in f:
            print(line.strip())


# print_file('playground/kudus/lab1.txt')

def list_folder_content(folder_path):
    try:
        print(os.listdir(folder_path))
    except Exception as e:
        print(e)


list_folder_content(os.getcwd())
