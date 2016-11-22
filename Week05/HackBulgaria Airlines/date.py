class Date:
    def __init__(self, day, month, year):
        Date._check_year(year)
        Date._check_month(month)
        Date._check_day(day, month, year)
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{}.{}.{}".format(self.day, self.month, self.year)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    def __hash__(self):
        return hash(self.day * self.month * self.year)

    def __lt__(self, other):
        return self.year < other.year\
            or (self.year == other.year and self.month < other.month)\
            or (self.year == other.year and self.month == other.month and self.day < other.day)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not(self <= other)

    def __ge__(self, other):
        return not(self < other)

    @classmethod
    def from_str(cls, date_str):
        day = int(date_str.split('.')[0])
        month = int(date_str.split('.')[1])
        year = int(date_str.split('.')[2])
        return Date(day, month, year)

    @classmethod
    def _check_day(cls, day, month, year):
        if day < 1 or day > 31:
            raise ValueError("Invalid day for date.")
        if day == 31 and (month == 4 or month == 6 or month == 9 or month == 11):
            raise ValueError("The day cannot be 31 in month".format(month))
        if month == 2 and day > 29:
            raise ValueError("February doesn't have more than 29 days.")
        if month == 2 and day == 29:
            if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):  # common year
                raise ValueError("February in Common year has only 28 days.")
        return True

    @classmethod
    def _check_month(cls, month):
        if type(month) is not int:
            raise TypeError("Month in date must be int.")
        if month < 1 or month > 12:
            raise ValueError("Invalid month.")
        return True

    @classmethod
    def _check_year(cls, year):
        if type(year) is not int:
            raise TypeError("Year in date must be int.")
        if year < 1980 or year > 2017:
            raise ValueError("Invalid year.")
        return True
