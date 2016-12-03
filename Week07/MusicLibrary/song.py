from hour import Hour


class Song:
    def __init__(self, title, artist, album, length_):
        self.title = title
        self.artist = artist
        self.album = album
        self.length_ = Hour(length_)

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length_)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.title == other.title\
            and self.artist == other.artist\
            and self.album == other.album\
            and self.length_ == other.length_

    def __hash__(self):
        return hash(self.title)*hash(self.artist)*hash(self.album)*hash(self.length_)

    def length(self, hours=False, minutes=False, seconds=False):
        if hours:
            return self.length_.get_hours()
        if minutes:
            return self.length_.get_minutes()
        if seconds:
            return self.length_.get_seconds()
        return str(self.length_)

    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def get_album(self):
        return self.album

    def get_length(self):
        return self.length_
