import unittest
from terminal import Terminal
from flight import Flight
from date_hour import DateHour
from date import Date


class TestTerminal(unittest.TestCase):
    def setUp(self):
        self.term_1 = Terminal(1, 20)
        self.term_2 = Terminal(2, 15)

    def test_eq(self):
        self.assertEqual(self.term_1, Terminal(1, 20))
        self.assertNotEqual(self.term_1, self.term_2)

    def test_add_flight(self):
        flight = Flight(DateHour(18, 11, 2016, "12:00"), DateHour(18, 11, 2016, "16:20"), 100, 120, "Sofia", "Madrid", self.term_1)
        self.assertIn(flight, self.term_1.flights)

    def test_get_terminal_flights(self):
        flight_1 = Flight(DateHour(18, 11, 2016, "12:00"), DateHour(18, 11, 2016, "16:20"), 100, 120, "Sofia", "Madrid", self.term_1)
        flight_2 = Flight(DateHour(19, 11, 2016, "15:45"), DateHour(19, 11, 2016, "20:30"), 100, 120, "Sofia", "London", self.term_1)
        flight_3 = Flight(DateHour(18, 11, 2016, "22:00"), DateHour(19, 11, 2016, "00:55"), 100, 120, "Sofia", "Berlin", self.term_1)
        flights = [flight_1, flight_2, flight_3]
        self.assertEqual(self.term_1.get_terminal_flights(), flights)

    def test_get_terminal_flights_on(self):
        flight_1 = Flight(DateHour(18, 11, 2016, "12:00"), DateHour(18, 11, 2016, "16:20"), 100, 120, "Sofia", "Madrid", self.term_1)
        flight_2 = Flight(DateHour(19, 11, 2016, "15:45"), DateHour(19, 11, 2016, "20:30"), 100, 120, "Sofia", "London", self.term_1)
        flight_3 = Flight(DateHour(18, 11, 2016, "22:00"), DateHour(19, 11, 2016, "00:55"), 100, 120, "Sofia", "Berlin", self.term_1)
        flights = [flight_1, flight_3]
        self.assertEqual(self.term_1.get_terminal_flights_on(Date(18, 11, 2016)), flights)

    def test_get_terminal_flights_to_dest(self):
        flight_1 = Flight(DateHour(18, 11, 2016, "12:00"), DateHour(18, 11, 2016, "16:20"), 100, 120, "Sofia", "Madrid", self.term_1)
        flight_2 = Flight(DateHour(19, 11, 2016, "15:45"), DateHour(19, 11, 2016, "20:30"), 100, 120, "Sofia", "London", self.term_1)
        flight_3 = Flight(DateHour(18, 11, 2016, "22:00"), DateHour(19, 11, 2016, "00:55"), 100, 120, "Sofia", "Berlin", self.term_1)
        flights = [flight_2]
        self.assertEqual(self.term_1.terminal_flights_to_dest("London"), flights)


if __name__ == '__main__':
    unittest.main()
