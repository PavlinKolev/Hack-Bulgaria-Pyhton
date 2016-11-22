from date import Date
from date_hour import DateHour
from hour import Hour
from flight import Flight
from terminal import Terminal
from passenger import Passenger
from reservation import Reservation


class Airport:
    def __init__(self, flights, passengers, reservations=[]):
        self.flights = flights
        self.passengers = passengers
        self.reservations = reservations

    def get_flights_for_date(self, date):
        res = []
        for fl in self.flights:
            if fl.get_date() == date:
                res.append(fl)
        return res

    def get_flights_before(self, date, hour):
        exact_time = DateHour.from_date_and_hour(date, hour)
        res = []
        for fl in self.flights:
            if fl.start_time <= exact_time:
                res.append(fl)
        return res

    def get_flights_from(self, destination):
        res = []
        for fl in self.flights:
            if fl.from_dest == destination:
                res.append(fl)
        return res

    def get_flights_to(self, destination):
        res = []
        for fl in self.flights:
            if fl.to_dest == destination:
                res.append(fl)
        return res

    def get_flight_to(self, destination, date):
        res = []
        for fl in self.flights:
            if fl.to_dest == destination and fl.get_date() == date:
                res.append(fl)
        return res

    def get_flight_from(self, destination, date):
        res = []
        for fl in self.flights:
            if fl.from_dest == destination and fl.get_date() == date:
                res.append(fl)
        return res

    def flights_on_date_lt_hours(self, date, hours):
        res = []
        for fl in self.flights:
            if fl.get_date() == date and fl.flight_duration() < Hour(hours):
                res.append(fl)
        return res

    def flights_within_duration(self, start_time, end_time):
        res = []
        for fl in self.flights:
            if fl.start_time >= start_time and fl.end_time <= end_time:
                res.append(fl)
        return res

    def passengers_under_18(self, flight):
        res = []
        for psng in self.passengers:
            if psng.flight == flight and psng.age < 18:
                res.append(psng)
        return res

    def passengers_to_dest(self, destination):
        res = []
        for psn in self.passengers:
            if psn.flight.to_dest == destination:
                res.append(psn)
        return res

    def passengers_from_terminal(self, terminal):
        res = []
        for psn in self.passengers:
            if psn.flight.terminal == terminal:
                res.append(psn)
        return res

    def flights_with_passengers(self, size):
        res = []
        for fl in self.flights:
            if fl.psng_count > size:
                res.append(fl)
        return res

    def passengers_reservations(self, flight):
        res = []
        for reservation in self.reservations:
            if reservation.flight == flight:
                res.append(reservation)
        return res

    def reservations_to_destination(self, destination):
        res = []
        for reservation in self.reservations:
            if reservation.flight.to_dest == destination:
                res.append(reservation)
        return res
