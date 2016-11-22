from hour import Hour
from date import Date


class DateHour(Date):
    def __init__(self, day, month, year, hour):
        Date.__init__(self, day, month, year)
        self.hour = Hour(hour)

    def __str__(self):
        date_str = Date.__str__(self)
        return date_str + " - " + str(self.hour)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return Date.__eq__(self, other) and self.hour == other.hour

    def __hash__(self):
        if self.hour != Hour("00:00"):
            return hash(Date.__hash__(self) * hash(self.hour))
        return hash(Date.__hash__(self))

    def __lt__(self, other):
        return Date.__lt__(self, other) or (Date.__eq__(self, other) and self.hour < other.hour)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not(self <= other)

    def __ge__(self, other):
        return not(self < other)

    def get_date(self):  # returns the date as Date object
        return Date(self.day, self.month, self.year)

    @classmethod
    def duration_in_hours(cls, date_1, date_2):
        return date_1.hour - date_2.hour

    @classmethod
    def from_date_and_hour(cls, date, hour):
        return DateHour(date.day, date.month, date.year, hour)
