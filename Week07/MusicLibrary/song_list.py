import json
from collections import OrderedDict
from random import randint
from prettytable import PrettyTable
from song import Song
from hour import Hour


class SongList:
    def __init__(self):
        self.songs = []
        self.curr_song_ind = -1
        self.artists_hist = {}
        self.played_songs = []

    def __all_songs(self):
        return self.songs + self.played_songs

    def add_song(self, song):
        if type(song) is not Song:
            raise TypeError("Type of song is not Song.")
        self.songs.append(song)
        self.__icr_artist_songs(song)

    def remove_song(self, song):
        if type(song) is not Song:
            raise TypeError("Type of song is not Song.")
        if song not in self.songs:
            raise "Song is not in playlist."
        self.songs.remove(song)
        self.__decr_artist_songs(song)

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def __icr_artist_songs(self, song):
        if song.get_artist() not in self.artists_hist:
            self.artists_hist[song.get_artist()] = 1
        else:
            self.artists_hist[song.get_artist()] += 1

    def __decr_artist_songs(self, song):
        self.artists_hist[song.get_artist()] -= 1

    def total_length(self):
        total = Hour("00:00:00")
        for song in self.__all_songs():
            total += song.get_length()
        return str(total)

    def artists(self):
        for artist in self.artists_hist:
            if self.artists_hist[artist] <= 0:
                del self.artists_hist[artist]
        ordered = OrderedDict((sorted(self.artists_hist.items())))
        return ordered

    def next_song(self, repeat, shuffle):
        if repeat:
            return self.__song_repeat_TRUE(shuffle)
        return self.__song_repeat_FALSE(shuffle)

    def __song_repeat_TRUE(self, shuffle):
        if self.__all_songs_are_played():
            self.curr_song_ind += 1
            self.curr_song_ind %= len(self.played_songs)
            return self.played_songs[self.curr_song_ind]
        return self.__song_depends_on_shuffle(shuffle)

    def __song_repeat_FALSE(self, shuffle):
        if self.__all_songs_are_played():
            print("All songs are played.")
            return False
        return self.__song_depends_on_shuffle(shuffle)

    def __all_songs_are_played(self):
        return self.songs == []

    def __song_depends_on_shuffle(self, shuffle):
        index = 0
        if shuffle:
            index = randint(0, len(self.songs) - 1)
        self.played_songs.append(self.songs[index])
        self.songs.pop(index)
        return self.played_songs[-1]

    def pprint(self):
        table = PrettyTable()
        table.field_names = ["Artist", "Song", "Length"]
        for song in self.__all_songs():
            table.add_row([song.get_artist(), song.get_title(), song.length()])
        print(table)

    def get_json_songs(self):
        song_list = []
        for song in self.__all_songs():
            song_list.append(OrderedDict([["title", song.get_title()],
                                            ["artist", song.get_artist()],
                                            ["album", song.get_album()],
                                            ["length", song.length()]]))
        return song_list
