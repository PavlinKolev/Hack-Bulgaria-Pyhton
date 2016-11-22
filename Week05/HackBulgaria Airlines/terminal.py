class Terminal:
    def __init__(self, number, max_flights):
        if type(number) is not int or type(max_flights) is not int:
            raise TypeError("Number and max_flights in Terminal must be int")
        if number <= 0 or max_flights <= 0:
            raise ValueError("Number and max_flights in Terminal cannot be negative or zero.")
        self.number = number
        self.max_flights = max_flights
        self.flights = []

    def __eq__(self, other):
        return self.number == other.number and self.max_flights == other.max_flights

    def add_flight(self, flight):
        if len(self.flights) >= self.max_flights:
            raise OverflowError("The limit of flights in terminal is reached.")
        self.flights.append(flight)

    def get_terminal_flights(self):
        return self.flights

    def get_terminal_flights_on(self, date):
        res = []
        for fl in self.flights:
            if fl.get_date() == date:
                res.append(fl)
        return res

    def terminal_flights_to_dest(self, destination):
        res = []
        for fl in self.flights:
            if fl.to_dest == destination:
                res.append(fl)
        return res
