import os
from sys import argv


def main():
    path = argv[1]
    try:
        total_sum = 0
        for root, dirs, files in os.walk(path):
            for file_name in files:
                full_file_name = root + '/' + file_name
                size = os.path.getsize(full_file_name)
                total_sum += size
        print("Total Sum: ", total_sum)
    except FileNotFoundError as error:
        print(error)


if __name__ == '__main__':
    main()
