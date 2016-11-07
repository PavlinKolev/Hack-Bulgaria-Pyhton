from sys import argv
from polynom import Polynom


def main():
    p = Polynom(argv[1])
    p.print_derivative()


if __name__ == '__main__':
    main()
