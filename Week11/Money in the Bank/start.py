from main_menu import MainMenu


def main():
    menu = MainMenu()
    menu.run()


def test():
    d = {"kaka": 5, "pedal": 7}
    c = input(":> ")
    print(d[c])


if __name__ == '__main__':
    main()
