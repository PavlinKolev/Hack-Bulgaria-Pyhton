class Hour:
    def __init__(self, hour_str):
        hour = hour_str.split(':')
        hour.reverse()
        self.sec = int(hour[0])
        self.min = int(hour[1])
        self.hour = int(hour[2]) if len(hour) is 3 else 0

    def __str__(self):
        if self.hour != 0:
            return "{}:{:02d}:{:02d}".format(self.hour, self.min, self.sec)
        return "{:02d}:{:02d}".format(self.min, self.sec)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.sec == other.sec\
            and self.min == other.min\
            and self.hour == other.hour

    def __hash__(self):
        result = 1
        if self.hour != 0:
            result *= self.hour
        if self.min != 0:
            result *= self.min
        if self.sec != 0:
            result *= self.sec
        return hash(result)

    def __add__(self, other):
        new_sec = self.sec + other.sec
        new_min = self.min + other.min
        new_hour = self.hour + other.hour
        if new_sec >= 60:
            new_sec -= 60
            new_min += 1
        if new_min >= 60:
            new_min -= 60
            new_hour += 1
        return Hour("{}:{}:{}".format(new_hour, new_min, new_sec))

    def get_seconds(self):
        return self.hour * 3600 + self.min * 60 + self.sec

    def get_minutes(self):
        return self.hour * 60 + self.min

    def get_hours(self):
        return self.hour
