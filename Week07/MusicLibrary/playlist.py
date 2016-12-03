import os.path
import json
from collections import OrderedDict
from song import Song
from song_list import SongList


class Playlist:
    DEFAULT_FOLDER = "playlist-data/"

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songList = SongList()

    def change_repeat(self, repeat):
        if type(repeat) is not bool:
            raise TypeError("Type of repeat must be boolean.")
        self.repeat = repeat

    def change_shuffle(self, shuffle):
        if type(shuffle) is not bool:
            raise TypeError("Type of repeat must be boolean.")
        self.shuffle = shuffle

    def add_song(self, song):
        self.songList.add_song(song)

    def remove_song(self, song):
        self.songList.remove_song(song)

    def add_songs(self, songs):
        self.songList.add_songs(songs)

    def total_length(self):
        return self.songList.total_length()

    def artists(self):
        return self.songList.artists()

    def next_song(self):
        return self.songList.next_song(self.repeat, self.shuffle)

    def pprint_playlist(self):
        self.songList.pprint()

    def save(self):
        file_name = Playlist.DEFAULT_FOLDER + self.name.replace(' ', '-') + ".json"
        json_objects = OrderedDict([["name", self.name], ["repeat", self.repeat], ["shuffle", self.shuffle]])
        json_objects["songs"] = self.songList.get_json_songs()
        with open(file_name, 'w') as f:
            json.dump(json_objects, f, indent=4)

    @staticmethod
    def load(path):
        path = Playlist.check_path(path)
        with open(path, 'r') as f:
            data = json.load(f)
            playlist = Playlist(data["name"], data["repeat"], data["shuffle"])
            for song in data["songs"]:
                playlist.add_song(Song(song["title"], song["artist"], song["album"], song["length"]))
            return playlist

    @staticmethod
    def check_path(path):
        if not(path.endswith(".json")):
            raise TypeError("Not a valid json file!")
        if os.path.isfile(path):
            return path
        elif os.path.isfile(Playlist.DEFAULT_FOLDER + path):
            return Playlist.DEFAULT_FOLDER + path
        raise TypeError("Cannot find the wanted file.")
