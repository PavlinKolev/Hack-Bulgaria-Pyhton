from flight import Flight


class Passenger:
    def __init__(self, first_name, last_name, flight, age):
        self.first_name = first_name
        self.last_name = last_name
        self.flight = flight
        self.age = age
        self.flight.add_passng(self)

    def __eq__(self, other):
        return self.first_name == other.first_name\
            and self.last_name == other.last_name\
            and self.age == other.age
