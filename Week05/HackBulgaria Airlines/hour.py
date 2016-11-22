class Hour:
    def __init__(self, hour_str):
        self.h = int(hour_str.split(':')[0])
        self.min = int(hour_str.split(':')[1])
        Hour._check_hour(self.h)
        Hour._check_minutes(self.min)

    def __str__(self):
        return "{}:{}".format(self.h, self.min)

    def __repr__(self):
        return self.__str__()

    def __sub__(self, other):
        h = self.h - other.h
        minutes = self.min - other.min
        if h < 0:
            h += 24
        if minutes < 0:
            minutes += 60
            if h == 0:
                h = 23
            else:
                h -= 1
        return Hour.from_numbers(h, minutes)

    def __eq__(self, other):
        return self.h == other.h and self.min == other.min

    def __hash__(self):
        if self.h != 0 and self.min != 0:
            return hash(self.h * self.min)
        if self.h == 0:
            return hash(self.min)
        return hash(self.h)

    def __lt__(self, other):
        return self.h < other.h or (self.h == other.h and self.min < other.min)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not(self <= other)

    def __ge__(self, other):
        return not(self < other)

    @classmethod
    def from_numbers(cls, h, minutes):
        return Hour("{}:{}".format(h, minutes))

    @classmethod
    def _check_hour(cls, h):
        if h < 0 or h > 23:
            raise ValueError("Hour must be in range(0, 23).")
        return True

    @classmethod
    def _check_minutes(cls, minutes):
        if minutes < 0 or minutes > 59:
            raise ValueError("Minutes must be in range(0, 59).")
        return True
