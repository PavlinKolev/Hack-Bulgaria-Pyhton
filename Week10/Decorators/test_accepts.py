import unittest
from accepts_decorator import accepts


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def deposit(name, money):
    return "{} sends {} $!".format(name, money)


@accepts(str, str, int)
def own_money(person_1, person_2, money):
    return "{} owns {} $ to {}".format(person_1, money, person_2)


class TestAcceptsDecorator(unittest.TestCase):
    def __setUp__(self):
        pass

    def test_funtion_pass_1(self):
        expected = "Hello, I am Gosho"
        self.assertEqual(say_hello("Gosho"), expected)

    def test_funtion_pass_2(self):
        expected = "Pesho sends 500 $!"
        self.assertEqual(deposit("Pesho", 500), expected)

    def test_funtion_pass_3(self):
        expected = "Gosho owns 500 $ to Pesho"
        self.assertEqual(own_money("Gosho", "Pesho", 500), expected)

    def test_type_error_1(self):
        self.assertRaises(TypeError, say_hello, 4)

    def test_type_error_2(self):
        self.assertRaises(TypeError, deposit, "Pesho", "Gosho")

    def test_type_error_3(self):
        self.assertRaises(TypeError, own_money, 5, 2, 3)

    def test_different_lengths(self):
        self.assertRaises(TypeError, say_hello, "Pesho", 100, 200)


if __name__ == '__main__':
    unittest.main()
