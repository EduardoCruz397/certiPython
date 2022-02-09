import os

def get_first_line(filename, mode):
    if os.path.isfile(filename):
        with open(filename, mode) as file:
            return file.readline()
    else:
        return None

print(get_first_line('texto.txt', 'r'))