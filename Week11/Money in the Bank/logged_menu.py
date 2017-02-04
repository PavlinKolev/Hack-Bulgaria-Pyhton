import os


class LoggedMenu:
    def __init__(self, manager):
        self.logged_user = None
        self.manager = manager
        self.commands = self.__get_commands()

    def run(self, logged_user):
        self.logged_user = logged_user
        print("Welcome you are logged in as: " + self.logged_user.get_username())
        while True:
            os.system('clear')
            command = input("Logged>>")
            try:
                self.commands[command]()
            except KeyError:
                print("Not a valid command")
            except ValueError as e:
                print(e)
            finally:
                input("\nPress Enter to continue...")

    def __info(self):
        print("You are: " + self.logged_user.get_username())
        print("Your id is: {}".format(self.logged_user.get_id()))
        print("Your balance is: {} $".format(self.logged_user.get_balance()))

    def __change_pass(self):
        new_pass = input("Enter your new password: ")
        self.manager.change_pass_of_client(new_pass, logged_user)

    def __change_message(self):
        new_message = input("Enter your new message: ")
        self.manager.change_message_of_client(new_message, logged_user)

    def __show_message(self):
        print(self.logged_user.get_message())

    def __help(self):
        print("info - for showing account info")
        print("changepass - for changing passowrd")
        print("change-message - for changing users message")
        print("show-message - for showing users message")

    def __get_commands(self):
        return {'info': self.__info,
                'changepass': self.__change_pass,
                'change-message': self.__change_message,
                'show-message': self.__show_message,
                'help': self.__help}
