from terminal import Terminal
from date_hour import DateHour


class Flight:
    def __init__(self, start_time, end_time, passengers, max_passengers, from_dest, to_dest, terminal, declined=False):
        if start_time >= end_time:
            raise ValueError("Start time cannot be after end time in flight.")
        if passengers > max_passengers:
            raise ValueError("Passengers cannot be over max_passengers.")
        self.start_time = start_time
        self.end_time = end_time
        self.psng_count = passengers
        self.max_passengers = max_passengers
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.terminal = terminal
        self.declined = declined
        self.passngs = []
        self.terminal.add_flight(self)

    def __eq__(self, other):
        return self.start_time == other.start_time\
            and self.end_time == other.end_time\
            and self.psng_count == other.psng_count\
            and self.max_passengers == other.max_passengers\
            and self.to_dest == other.to_dest\
            and self.terminal == other.terminal

    def get_date(self):  # returns the date as Date object for start_time
        return self.start_time.get_date()

    def flight_duration(self):
        return DateHour.duration_in_hours(self.end_time, self.start_time)

    def add_passng(self, passng):
        self.passngs.append(passng)

    def flight_empty_seats(self):
        return self.max_passengers - self.psng_count
