import unittest
from date import Date


class TestDate(unittest.TestCase):
    def setUp(self):
        self.date_1 = Date(27, 11, 2016)
        self.date_2 = Date(29, 11, 2016)

    def test_str(self):
        self.assertEqual(str(self.date_1), "27.11.2016")
        self.assertEqual(str(self.date_2), "29.11.2016")

    def test_eq(self):
        self.assertEqual(self.date_1, Date(27, 11, 2016))
        self.assertNotEqual(self.date_1, self.date_2)

    def test_hash(self):
        self.assertEqual(hash(self.date_1), hash(Date(27, 11, 2016)))
        self.assertNotEqual(hash(self.date_1), hash(self.date_2))

    def test_lt(self):
        self.assertTrue(self.date_1 < self.date_2)

    def test_le(self):
        self.assertTrue(self.date_1 <= self.date_2)
        self.assertTrue(self.date_1 <= Date(27, 11, 2016))

    def test_gt(self):
        self.assertTrue(self.date_2 > self.date_1)

    def test_ge(self):
        self.assertTrue(self.date_2 >= self.date_1)
        self.assertTrue(self.date_2 >= Date(29, 11, 2016))

    def test_from_str(self):
        date = Date.from_str("15.09.2000")
        self.assertEqual(date, Date(15, 9, 2000))

    def test_check_day(self):
        self.assertTrue(Date._check_day(1, 1, 2016))
        self.assertTrue(Date._check_day(31, 12, 2016))
        self.assertTrue(Date._check_day(29, 2, 2016))
        self.assertRaises(ValueError, Date._check_day, 29, 2, 2015)
        self.assertRaises(ValueError, Date._check_day, 31, 4, 2016)
        self.assertRaises(ValueError, Date._check_day, 32, 12, 2016)

    def test_month(self):
        self.assertTrue(Date._check_month(1))
        self.assertTrue(Date._check_month(12))
        self.assertRaises(ValueError, Date._check_month, 0)
        self.assertRaises(ValueError, Date._check_month, 13)

    def test_year(self):
        self.assertTrue(Date._check_year(1980))
        self.assertTrue(Date._check_year(2017))
        self.assertRaises(ValueError, Date._check_year, 1979)
        self.assertRaises(ValueError, Date._check_year, 2018)


if __name__ == '__main__':
    unittest.main()
