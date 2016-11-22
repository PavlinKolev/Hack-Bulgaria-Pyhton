import unittest
from airport import Airport
from flight import Flight
from terminal import Terminal
from passenger import Passenger
from reservation import Reservation
from date_hour import DateHour
from date import Date
from hour import Hour


terminal_1 = Terminal(1, 20)
terminal_2 = Terminal(2, 15)

flight_1 = Flight(DateHour(18, 11, 2016, "12:00"), DateHour(18, 11, 2016, "16:20"), 100, 120, "Sofia", "Madrid", terminal_1)
flight_2 = Flight(DateHour(19, 11, 2016, "15:45"), DateHour(19, 11, 2016, "20:30"), 80, 120, "Sofia", "London", terminal_1)
flight_3 = Flight(DateHour(18, 11, 2016, "20:00"), DateHour(19, 11, 2016, "00:55"), 85, 120, "Sofia", "Berlin", terminal_2)
flight_4 = Flight(DateHour(19, 11, 2016, "23:45"), DateHour(20, 11, 2016, "04:50"), 110, 120, "Sofia", "Lisbon", terminal_2)
flight_5 = Flight(DateHour(20, 11, 2016, "21:00"), DateHour(21, 11, 2016, "02:20"), 100, 120, "Sofia", "Stockholm", terminal_2)

psng_1 = Passenger("Ivan", "Georgiev", flight_1, 25)
psng_2 = Passenger("Petq", "Hristova", flight_2, 23)
psng_3 = Passenger("Georgi", "Ivanov", flight_3, 16)
psng_4 = Passenger("Pavlin", "Kolev", flight_4, 23)
psng_5 = Passenger("Maria", "Petrova", flight_5, 20)
psng_6 = Passenger("Petar", "Petrov", flight_1, 19)
psng_7 = Passenger("Martin", "Biserov", flight_2, 21)
psng_8 = Passenger("Georgi", "Petrov", flight_3, 30)
psng_9 = Passenger("Nikolay", "Petrov", flight_4, 29)
psng_10 = Passenger("Ana", "Velikova", flight_5, 26)

res_1 = Reservation(flight_1, psng_1)
res_2 = Reservation(flight_2, psng_2)
res_3 = Reservation(flight_3, psng_3)
res_4 = Reservation(flight_4, psng_4)
res_5 = Reservation(flight_5, psng_5)
res_6 = Reservation(flight_1, psng_6)
res_7 = Reservation(flight_2, psng_7)
res_8 = Reservation(flight_3, psng_8)
res_9 = Reservation(flight_4, psng_9)
res_10 = Reservation(flight_5, psng_10)

flights = [flight_1, flight_2, flight_3, flight_4, flight_5]
passengers = [psng_1, psng_2, psng_3, psng_4, psng_5, psng_6, psng_7, psng_8, psng_9, psng_10]
reservations = [res_1, res_2, res_3, res_4, res_5, res_6, res_7, res_8, res_9, res_10]


class TestAirport(unittest.TestCase):
    def setUp(self):
        self.airport = Airport(flights, passengers, reservations)

    def test_get_flights_for_date(self):
        date = Date(18, 11, 2016)
        flights = [flight_1, flight_3]
        self.assertEqual(self.airport.get_flights_for_date(date), flights)

    def test_get_flights_before(self):
        date = Date(19, 11, 2016)
        flights = [flight_1, flight_2, flight_3, flight_4]
        self.assertEqual(self.airport.get_flights_before(date, "23:59"), flights)

    def test_get_flights_from(self):
        flights = [flight_1, flight_2, flight_3, flight_4, flight_5]
        self.assertEqual(self.airport.get_flights_from("Sofia"), flights)

    def test_get_flights_to(self):
        flights = [flight_2]
        self.assertEqual(self.airport.get_flights_to("London"), flights)

    def test_flight_from(self):
        date = Date(18, 11, 2016)
        flights = [flight_1, flight_3]
        self.assertEqual(self.airport.get_flight_from("Sofia", date), flights)

    def test_flight_to(self):
        date = Date(18, 11, 2016)
        flights = [flight_1]
        self.assertEqual(self.airport.get_flight_to("Madrid", date), flights)

    def test_flights_on_date_lt_hours(self):
        date = Date(18, 11, 2016)
        flights = [flight_1]
        self.assertEqual(self.airport.flights_on_date_lt_hours(date, "04:25"), flights)

    def test_flights_within_duration(self):
        date = Date(18, 11, 2016)
        flights = [flight_1]
        self.assertEqual(self.airport.flights_on_date_lt_hours(date, "04:25"), flights)

    def test_passengers_under_18(self):
        self.assertEqual(self.airport.passengers_under_18(flight_3), [psng_3])

    def test_passengers_to_dest(self):
        passengers = [psng_2, psng_7]
        self.assertEqual(self.airport.passengers_to_dest("London"), passengers)

    def test_passengers_from_terminal(self):
        passengers = [psng_1, psng_2, psng_6, psng_7]
        self.assertEqual(self.airport.passengers_from_terminal(terminal_1), passengers)

    def test_flights_with_passengers(self):
        flights = [flight_1, flight_4, flight_5]
        self.assertEqual(self.airport.flights_with_passengers(90), flights)

    def test_passengers_reservations(self):
        reservations = [res_1, res_6]
        self.assertEqual(self.airport.passengers_reservations(flight_1), reservations)

    def test_reservations_to_destionation(self):
        reservations = [res_2, res_7]
        self.assertEqual(self.airport.reservations_to_destination("London"), reservations)


if __name__ == '__main__':
    unittest.main()
