import unittest
from validators import validate_client, validate_password, validate_username
from client import Client


class TestValidators(unittest.TestCase):
    def test_validate_client(self):
        self.assertTrue(validate_client(Client(1, "John", 5000, "Message")))

    def test_validate_client_except(self):
        self.assertRaises(TypeError, validate_client, 100)
        self.assertRaises(TypeError, validate_client, "string")

    def test_validate_username(self):
        self.assertTrue(validate_username("John"))
        self.assertTrue(validate_username("John_Smith"))

    def test_validate_username_except(self):
        self.assertRaises(ValueError, validate_username, "OR 1 = 1 --")
        self.assertRaises(ValueError, validate_username, "John  Smith ")
        self.assertRaises(ValueError, validate_username, "John\nSmith")

    def test_validate_password(self):
        self.assertTrue(validate_password("Abc123???", "John"))
        self.assertTrue(validate_password("Password1$", "John"))

    def test_validate_password_short(self):
        self.assertRaises(ValueError, validate_password, "ABC??12", "John")

    def test_validate_password_username_substr(self):
        self.assertRaises(ValueError, validate_password, "ABC?John?12", "John")

    def test_validate_password_no_upper(self):
        self.assertRaises(ValueError, validate_password, "abc?$$12345", "John")

    def test_validate_password_no_special(self):
        self.assertRaises(ValueError, validate_password, "abcABC12345", "John")

    def test_validate_password_no_digit(self):
        self.assertRaises(ValueError, validate_password, "abc?$$ABCd", "John")


if __name__ == '__main__':
    unittest.main()
