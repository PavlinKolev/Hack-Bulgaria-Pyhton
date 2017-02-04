import os
import sys
from sql_manager import SQL_Manager
from logged_menu import LoggedMenu


class MainMenu:
    def __init__(self):
        self.manager = SQL_Manager()
        self.logged_menu = LoggedMenu(self.manager)
        self.commands = self.__get_commands()

    def run(self):
        print("Welcome to our bank service. You are not logged in.")
        print("Please register or login")

        while True:
            os.system('clear')
            command = input("$$$>")
            try:
                self.commands[command]()
            except KeyError:
                print("Not a valid command")
            except ValueError as e:
                print(e)
            finally:
                input("\nPress Enter to continue...")

    def __register(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        self.manager.register_new_client(username, password)
        print("Registration Successfull")

    def __login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        logged_user = self.manager.login_client(username, password)

        if logged_user:
            self.logged_menu.run(logged_user)
        else:
            print("Login failed")

    def __help(self):
        print("login - for logging in!")
        print("register - for creating new account!")
        print("exit - for closing program!")

    def __exit(self):
        sys.exit()

    def __get_commands(self):
        return {'register': self.__register,
                'login': self.__login,
                'help': self.__help,
                'exit': self.__exit}
