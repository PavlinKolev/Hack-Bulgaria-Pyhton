from sys import argv


def wc_word(file_name):
    with open(file_name, 'r') as f:
        return len([word for word in f.read().split()])


def wc_char(file_name):
    with open(file_name, 'r') as f:
        chars = 0
        for line in f:
            chars += len(line)
        return chars


def wc_line(file_name):
    with open(file_name, 'r') as f:
        return len(f.readlines())


def execute_wc(option, file_name):
    if option == "words":
        return wc_word(file_name)
    elif option == "chars":
        return wc_char(file_name)
    elif option == "lines":
        return wc_line(file_name)
    else:
        raise ValueError("Wrong option in wc command.")


def main():
    option = argv[1]
    file_name = argv[2]
    print(execute_wc(option, file_name))


if __name__ == '__main__':
    main()
