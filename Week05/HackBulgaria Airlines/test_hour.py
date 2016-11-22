import unittest
from hour import Hour


class TestHour(unittest.TestCase):
    def setUp(self):
        self.h_1 = Hour("12:30")
        self.h_2 = Hour("22:50")

    def test_str(self):
        self.assertEqual(str(self.h_1), "12:30")
        self.assertEqual(str(self.h_2), "22:50")

    def test_eq(self):
        self.assertEqual(self.h_1, Hour("12:30"))
        self.assertNotEqual(self.h_1, self.h_2)

    def test_sub(self):
        # duration = end_time - start_time
        sub_1 = self.h_1 - self.h_2
        sub_2 = self.h_2 - self.h_1
        self.assertEqual(sub_1, Hour("13:40"))
        self.assertEqual(sub_2, Hour("10:20"))

    def test_hash(self):
        self.assertEqual(hash(self.h_1), hash(Hour("12:30")))
        self.assertNotEqual(hash(self.h_1), hash(Hour("12:31")))

    def test_lt(self):
        self.assertTrue(self.h_1 < self.h_2)

    def test_le(self):
        self.assertTrue(self.h_1 <= self.h_2)
        self.assertTrue(self.h_1 <= Hour("12:30"))

    def test_gt(self):
        self.assertTrue(self.h_2 > self.h_1)

    def test_ge(self):
        self.assertTrue(self.h_2 >= self.h_1)
        self.assertTrue(self.h_2 >= Hour("22:50"))

    def test_check_hour(self):
        self.assertTrue(Hour._check_hour(0))
        self.assertTrue(Hour._check_hour(23))
        self.assertTrue(Hour._check_hour(10))
        self.assertRaises(ValueError, Hour._check_hour, -1)
        self.assertRaises(ValueError, Hour._check_hour, 24)

    def test_check_minutes(self):
        self.assertTrue(Hour._check_minutes(0))
        self.assertTrue(Hour._check_minutes(59))
        self.assertTrue(Hour._check_minutes(10))
        self.assertRaises(ValueError, Hour._check_minutes, -1)
        self.assertRaises(ValueError, Hour._check_minutes, 60)


if __name__ == '__main__':
    unittest.main()
