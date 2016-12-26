from sys import argv


def read_file(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line.rstrip())


def main():
    for indx in range(1, len(argv)):
        read_file(argv[indx])
        print()

if __name__ == '__main__':
    main()
