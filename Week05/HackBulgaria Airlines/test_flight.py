import unittest
from flight import Flight
from terminal import Terminal
from passenger import Passenger
from date_hour import DateHour
from date import Date
from hour import Hour


class TestFlight(unittest.TestCase):
    def setUp(self):
        term = Terminal(1, 20)
        self.flight_1 = Flight(DateHour(18, 11, 2016, "12:00"), DateHour(18, 11, 2016, "16:20"), 100, 120, "Sofia", "Madrid", term)
        self.flight_2 = Flight(DateHour(19, 11, 2016, "15:45"), DateHour(19, 11, 2016, "20:30"), 90, 120, "Sofia", "London", term)

    def test_eq(self):
        flight = Flight(DateHour(18, 11, 2016, "12:00"), DateHour(18, 11, 2016, "16:20"), 100, 120, "Sofia", "Madrid", Terminal(1, 20))
        self.assertEqual(self.flight_1, flight)
        self.assertNotEqual(self.flight_1, self.flight_2)

    def test_get_date(self):
        self.assertEqual(self.flight_1.get_date(), Date(18, 11, 2016))
        self.assertEqual(self.flight_2.get_date(), Date(19, 11, 2016))

    def test_flight_duration(self):
        duration_1 = self.flight_1.flight_duration()
        duration_2 = self.flight_2.flight_duration()
        self.assertEqual(duration_1, Hour("04:20"))
        self.assertEqual(duration_2, Hour("04:45"))

    def test_add_passenger(self):
        p_1 = Passenger("Ivan", "Georgiev", self.flight_1, 20)
        p_2 = Passenger("Georgi", "Ivanov", self.flight_1, 22)
        self.assertIn(p_1, self.flight_1.passngs)
        self.assertIn(p_2, self.flight_1.passngs)

    def test_empty_seats(self):
        self.assertEqual(self.flight_1.flight_empty_seats(), 20)
        self.assertEqual(self.flight_2.flight_empty_seats(), 30)


if __name__ == '__main__':
    unittest.main()
