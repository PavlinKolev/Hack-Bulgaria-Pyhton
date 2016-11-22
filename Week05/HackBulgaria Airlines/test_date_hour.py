import unittest
from date_hour import DateHour
from date import Date
from hour import Hour


class TestDateHour(unittest.TestCase):
    def setUp(self):
        self.date_1 = DateHour(27, 11, 2016, "12:30")
        self.date_2 = DateHour(27, 11, 2016, "22:50")

    def test_str(self):
        self.assertEqual(str(self.date_1), "27.11.2016 - 12:30")
        self.assertEqual(str(self.date_2), "27.11.2016 - 22:50")

    def test_eq(self):
        self.assertEqual(self.date_1, DateHour(27, 11, 2016, "12:30"))
        self.assertNotEqual(self.date_1, DateHour(27, 11, 2016, "12:31"))

    def test_hash(self):
        self.assertEqual(hash(self.date_1), hash(DateHour(27, 11, 2016, "12:30")))
        self.assertNotEqual(hash(self.date_1), hash(self.date_2))

    def test_lt(self):
        self.assertTrue(self.date_1 < self.date_2)
        self.assertTrue(self.date_1 < DateHour(30, 11, 2016, "00:01"))


    def test_le(self):
        self.assertTrue(self.date_1 <= self.date_2)
        self.assertTrue(self.date_1 <= DateHour(27, 11, 2016, "12:30"))
        self.assertTrue(self.date_1 <= DateHour(31, 12, 2016, "12:30"))

    def test_gt(self):
        self.assertTrue(self.date_2 > self.date_1)
        self.assertTrue(self.date_2 > DateHour(1, 1, 1999, "12:00"))

    def test_ge(self):
        self.assertTrue(self.date_2 >= self.date_1)
        self.assertTrue(self.date_2 >= DateHour(27, 11, 2016, "22:50"))
        self.assertTrue(self.date_1 > DateHour(1, 1, 1999, "12:00"))

    def test_get_date(self):
        self.assertEqual(self.date_1.get_date(), self.date_2.get_date())

    def test_duration_in_hours(self):
        duration_hours = DateHour.duration_in_hours(self.date_2, self.date_1)
        self.assertEqual(str(duration_hours), "10:20")

    def test_from_date_and_hour(self):
        date = Date(31, 12, 2016)
        date_hour = DateHour.from_date_and_hour(date, "23:59")
        self.assertEqual(date_hour, DateHour(31, 12, 2016, "23:59"))


if __name__ == '__main__':
    unittest.main()
