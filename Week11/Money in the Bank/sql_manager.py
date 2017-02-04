import sqlite3
import datetime
from client import Client
from validators import validate_client, validate_password, validate_username
from password import encode
from queries import (CREATE_CLIENTS_TABLE, UPDATE_MESSAGE_OF_CLIENT, GET_ALL_USERAMES,
                    UPDATE_PASSWORD_OF_CLIENT, ADD_CLIENT, GET_CLIENT_DATA, GET_USERNAME_BY_ID,
                    GET_COUNT_TRIES, SET_COUNT_TRIES, GET_TIME_FOR_WRONG_TRIES,
                    SET_TIME_FOR_WRONG_TRIES, GET_TIME_BANNED, SET_TIME_BANNED)

#
#    I implemented the first six steps from the task
#
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

    def __get_time_bannded(self, username):
        self.cursor.execute(GET_TIME_BANNED, (username, ))
        time_str = self.cursor.fetchone()[0]
        return datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

    def __get_time_for_wrong_tries(self, username):
        # import ipdb; ipdb.set_trace()
        self.cursor.execute(GET_TIME_FOR_WRONG_TRIES, (username, ))
        time_str = self.cursor.fetchone()[0]
        return datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

    def __get_count_tries(self, username):
        self.cursor.execute(GET_COUNT_TRIES, (username, ))
        return self.cursor.fetchone()[0]

    def login_client(self, username, password):
        # import ipdb; ipdb.set_trace()
        self.__validate_existing_username(username)

        now = datetime.datetime.now()
        time_banned = self.__get_time_bannded(username)
        if now < time_banned:
            raise ValueError("You are banned! ")

        time_for_wrong_tries = self.__get_time_for_wrong_tries(username)
        self.cursor.execute(GET_CLIENT_DATA, (username, encode(password)))
        user = self.cursor.fetchone()
        # import ipdb; ipdb.set_trace()
        FF = now >= time_for_wrong_tries
        if now >= time_for_wrong_tries:
            if(user):
                return Client(user[0], username, user[1], user[2])
            else:
                one_minute = (now + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
                self.cursor.execute(SET_TIME_FOR_WRONG_TRIES, (one_minute, username))
                self.cursor.execute(SET_COUNT_TRIES, (1, username))
                self.db.commit()
                return False
        else:
            if(user):
                self.cursor.execute(SET_COUNT_TRIES, (0, username))
                self.cursor.execute(SET_TIME_FOR_WRONG_TRIES, (now.strftime("%Y-%m-%d %H:%M:%S"), username))
                self.db.commit()
                return Client(user[0], username, user[1], user[2])
            else:
                count = self.__get_count_tries(username)
                if count == 4:
                    self.cursor.execute(SET_COUNT_TRIES, (0, username))
                    self.cursor.execute(SET_TIME_FOR_WRONG_TRIES, (now.strftime("%Y-%m-%d %H:%M:%S"), username))
                    five_min = (now + datetime.timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")
                    self.cursor.execute(SET_TIME_BANNED, (five_min, username))
                    self.db.commit()
                else:
                    self.cursor.execute(SET_COUNT_TRIES, (count + 1, username))
                    self.db.commit()
                return False

    def __validate_existing_username(self, username):
        self.cursor.execute(GET_ALL_USERAMES)
        names = self.cursor.fetchall()
        if username not in [u[0] for u in names]:
            raise ValueError("There is no user with this username")

    def __validate_logged_user(self, logged_user):
        validate_client(logged_user)
        self.__validate_logged_user_id(logged_user.get_id())

    def __validate_logged_user_id(self, user_id):
        self.cursor.execute(GET_USERNAME_BY_ID, (user_id, ))
        username = self.cursor.fetchone()
        if username is None:
            raise ValueError("There is no client with id: {}".format(user_id))
