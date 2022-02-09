import os


if os.path.isfile('in.txt'):
    file = open('in.txt')
    print(file.read())
    file.close()