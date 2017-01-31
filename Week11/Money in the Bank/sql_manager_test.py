import sys
import os
import unittest
from sql_manager import SQL_Manager
from queries import GET_CLIENT_DATA
from password import encode


class SqlManagerTests(unittest.TestCase):
    first_call = True

    def setUp(self):
        self.manager = SQL_Manager("test_bank.db")
        if SqlManagerTests.first_call:
            self.manager.register_new_client('Dinko', 'D123?Inko123')
            self.manager.register_new_client('Tester', "Pass123$$")
            self.manager.register_new_client('Tester2', "Pass123$$")
            SqlManagerTests.first_call = False

    def test_register_new_client(self):
        self.manager.cursor.execute(GET_CLIENT_DATA, ('Dinko', encode('D123?Inko123')))
        count = len(self.manager.cursor.fetchall())
        self.assertEqual(count, 1)

    def test_login_client(self):
        logged_user = self.manager.login_client('Tester', "Pass123$$")
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = self.manager.login_client('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = self.manager.login_client('Tester', "Pass123$$")
        new_message = "podaivinototam"
        self.manager.change_message_of_client(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = self.manager.login_client('Tester2', "Pass123$$")
        new_password = "NewPass**123"
        self.manager.change_pass_of_client(new_password, logged_user)
        logged_user = self.manager.login_client('Tester2', new_password)
        self.assertEqual(logged_user.get_username(), 'Tester2')

    @classmethod
    def tearDownClass(cls):
        os.remove("test_bank.db")


if __name__ == '__main__':
    unittest.main()
