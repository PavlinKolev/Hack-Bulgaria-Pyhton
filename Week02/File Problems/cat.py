from sys import argv


def main():
    file_name = argv[1]

    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line.rstrip())


if __name__ == '__main__':
    main()
