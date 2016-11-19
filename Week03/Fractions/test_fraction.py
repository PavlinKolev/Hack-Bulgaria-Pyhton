import unittest
from fraction import Fraction


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.fr_1 = Fraction(2, 6)  # 1/3
        self.fr_2 = Fraction(1, 2)

    def test_str(self):
        self.assertEqual(str(self.fr_1), "1 / 3")
        self.assertEqual(str(self.fr_2), "1 / 2")

    def test_eq(self):
        self.assertTrue(self.fr_1 == Fraction(1, 3))
        self.assertFalse(self.fr_1 == self.fr_2)

    def test_add(self):
        fr_3 = Fraction(3, 5)
        res = self.fr_1 + fr_3
        self.assertEqual(res, Fraction(14, 15))
        res = self.fr_2 + fr_3
        self.assertEqual(res, Fraction(11, 10))

    def test_sub(self):
        fr_3 = Fraction(3, 5)
        res = self.fr_1 - fr_3
        self.assertEqual(res, Fraction(-4, 15))
        res = self.fr_2 - fr_3
        self.assertEqual(res, Fraction(-1, 10))

    def test_mul(self):
        fr_3 = Fraction(3, 5)
        res = self.fr_1 * fr_3
        self.assertEqual(res, Fraction(1, 5))
        res = self.fr_2 * fr_3
        self.assertEqual(res, Fraction(3, 10))


if __name__ == '__main__':
    unittest.main()
