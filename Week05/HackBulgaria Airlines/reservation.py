from flight import Flight
from passenger import Passenger


class Reservation:
    def __init__(self, flight, passenger, accepted=True):
        self.flight = flight
        self.passenger = passenger
        self.accepted = accepted

    def __eq__(self, other):
        return self.flight == other.flight\
            and self.passenger == other.passenger
