import sqlite3
from client import Client
from validators import validate_client, validate_password, validate_username
from password import encode
from queries import (CREATE_CLIENTS_TABLE, UPDATE_MESSAGE_OF_CLIENT,
                    UPDATE_PASSWORD_OF_CLIENT, ADD_CLIENT, GET_CLIENT_DATA, GET_USERNAME_BY_ID)


class SQL_Manager:
    def __init__(self, db_name="bank.db"):
        self.db = sqlite3.connect(db_name)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.create_clients_table()

    def create_clients_table(self):
        self.cursor.execute(CREATE_CLIENTS_TABLE)
        self.db.commit()

    def change_message_of_client(self, new_message, logged_user):
        self.__validate_logged_user(logged_user)
        self.cursor.execute(UPDATE_MESSAGE_OF_CLIENT, (new_message, logged_user.get_id()))
        logged_user.set_message(new_message)
        self.db.commit()

    def change_pass_of_client(self, new_pass, logged_user):
        validate_client(logged_user)
        self.__validate_logged_user(logged_user)
        validate_password(new_pass, logged_user.get_username())
        self.cursor.execute(UPDATE_PASSWORD_OF_CLIENT, (encode(new_pass), logged_user.get_id()))
        self.db.commit()

    def register_new_client(self, username, password):
        validate_username(username)
        validate_password(password, username)
        self.cursor.execute(ADD_CLIENT, (username, encode(password)))
        self.db.commit()

    def login_client(self, username, password):
        self.cursor.execute(GET_CLIENT_DATA, (username, encode(password)))
        user = self.cursor.fetchone()
        if(user):
            return Client(user[0], username, user[1], user[2])
        return False

    def __validate_logged_user(self, logged_user):
        validate_client(logged_user)
        self.__validate_logged_user_id(logged_user.get_id())

    def __validate_logged_user_id(self, user_id):
        self.cursor.execute(GET_USERNAME_BY_ID, (user_id, ))
        username = self.cursor.fetchone()
        if username is None:
            raise ValueError("There is no client with id: {}".format(user_id))
