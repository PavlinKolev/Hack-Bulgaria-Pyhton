import unittest
from encrypt_decorator import encrypt


@encrypt(2)
def get_low():
    return "Get get get low"


@encrypt(3)
def say_hello(name):
    return "Hello, I am {}".format(name)


@encrypt(4)
def deposit(name, money):
    return "{} sends {} $!".format(name, money)


@encrypt(2)
def get_int():
    return 100


class TestEncryptDecorator(unittest.TestCase):
    def __setUp__(self):
        pass

    def test_funtion_pass_1(self):
        expected = "Igv igv igv nqy"
        self.assertEqual(get_low(), expected)

    def test_funtion_pass_2(self):
        expected = "Khoor, L dp Jrvkr"
        self.assertEqual(say_hello("Gosho"), expected)

    def test_funtion_pass_3(self):
        expected = "Tiwls wirhw 500 $!"
        self.assertEqual(deposit("Pesho", 500), expected)

    def test_type_error(self):
        self.assertRaises(TypeError, get_int)


if __name__ == '__main__':
    unittest.main()
