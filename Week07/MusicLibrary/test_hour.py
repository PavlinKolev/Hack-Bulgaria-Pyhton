import unittest
from hour import Hour


class TestHour(unittest.TestCase):
    def setUp(self):
        self.h_1 = Hour("12:53:29")
        self.h_2 = Hour("5:55")

    def test_str(self):
        self.assertEqual(str(self.h_1), "12:53:29")
        self.assertEqual(str(self.h_2), "05:55")

    def test_eq(self):
        self.assertEqual(self.h_1, Hour("12:53:29"))
        self.assertEqual(self.h_2, Hour("5:55"))
        self.assertNotEqual(self.h_1, self.h_2)

    def test_hash(self):
        self.assertEqual(hash(self.h_1), hash(Hour("12:53:29")))
        self.assertEqual(hash(self.h_2), hash(Hour("05:55")))

    def test_add(self):
        h_3 = self.h_1 + self.h_2
        self.assertEqual(h_3, Hour("12:59:24"))

    def test_get_seconds(self):
        self.assertEqual(self.h_1.get_seconds(), 46409)
        self.assertEqual(self.h_2.get_seconds(), 355)

    def test_get_minutes(self):
        self.assertEqual(self.h_1.get_minutes(), 773)
        self.assertEqual(self.h_2.get_minutes(), 5)

    def test_get_hours(self):
        self.assertEqual(self.h_1.get_hours(), 12)
        self.assertEqual(self.h_2.get_hours(), 0)


if __name__ == '__main__':
    unittest.main()
