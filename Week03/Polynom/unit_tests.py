import unittest
from polynom import Polynom
from monomial import Monomial

class TestPolynom(unittest.TestCase):
    def setUp(self):
        self.poly_1 = Polynom("3x^5 + 2x^5 + 4x^3 + 5 + 2")

    def test_str(self):
        result = "5*x^5 + 4*x^3 + 7"
        self.assertEqual(str(self.poly_1), result)

    def tets_derivative_1(self):
        derivat = "25*x^4 + 12*x^2"
        self.assertEqual(str(poly_1.derivative()), derivat)

    def test_derivative_2(self):
        poly = Polynom("x")
        self.assertEqual(str(poly.derivative()), "1")

    def test_derivative_3(self):
        poly = Polynom("175")
        self.assertEqual(str(poly.derivative()), "0")

    def test_derivative_4(self):
        poly = Polynom("x^2")
        self.assertEqual(str(poly.derivative()), "2*x")


class TestMonomial(unittest.TestCase):
    def setUp(self):
        self.mon_1 = Monomial(5, 2, 'x')
        self.mon_2 = Monomial(3, 4, 'x')

    def test_str(self):
        self.assertEqual(str(self.mon_1), "5*x^2")
        self.assertNotEqual(str(self.mon_1), str(self.mon_2))

    def test_add(self):
        mon_3 = Monomial(12, 2, 'x')
        self.assertEqual(str(self.mon_1 + mon_3), "17*x^2")

    def test_eq(self):
        self.assertFalse(self.mon_1 == self.mon_2)
        self.assertTrue(self.mon_1 == Monomial(5, 2, 'x'))

    def test_lt(self):
        self.assertTrue(self.mon_1 < self.mon_2)
        self.assertFalse(self.mon_2 < self.mon_1)

    def test_gt(self):
        self.assertFalse(self.mon_1 > self.mon_2)
        self.assertTrue(self.mon_2 > self.mon_1)

    def test_hash(self):
        self.assertEqual(self.mon_1.__hash__(), Monomial(5, 2, 'x').__hash__())
        self.assertNotEqual(self.mon_1.__hash__(), self.mon_2.__hash__())

    def test_derivative(self):
        dev = Monomial(10, 1, 'x')
        self.assertEqual(self.mon_1.derivative(), dev)
        self.assertNotEqual(self.mon_2.derivative(), dev)


if __name__ == '__main__':
    unittest.main()
