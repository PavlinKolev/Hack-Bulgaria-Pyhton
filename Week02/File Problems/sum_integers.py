from sys import argv


def main():
    file_name = argv[1]
    f = open(file_name, "r")
    sum_ = 0
    for line in f:
        numbers = line.split(' ')
        numbers.pop()  # remove '\n'
        for x in numbers:
            sum_ += int(x)
    f.close()
    print(sum_)


if __name__ == '__main__':
    main()
