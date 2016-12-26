from sys import argv
from random import randint
from cat_multiple import read_file


def main():
    file_name = argv[1]
    number_count = int(argv[2])

    f = open(file_name, "w")
    for indx in range(number_count):
        rand_num = randint(1, 1000)
        f.write(str(rand_num))
        f.write(' ')

    f.close()


if __name__ == '__main__':
    main()
