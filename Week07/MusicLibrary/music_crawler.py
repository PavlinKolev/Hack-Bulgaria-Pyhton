import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from song import Song
from playlist import Playlist


def to_hour_str(seconds):
    return "{}:{}:{}".format(
        int(seconds//3600),
        int((seconds % 3600)//60),
        int((seconds % (3600*60)) % 60))


class MusicCrawler:
    def __init__(self, music_path):
        MusicCrawler.check_path(music_path)
        self.music_path = music_path

    def generate_playlist(self):
        playlist_name = self.music_path.split('/')[-1]
        playlist = Playlist(playlist_name)
        for audio_file in os.listdir(self.music_path):
            if audio_file.endswith(".mp3"):
                mp3 = MP3(self.music_path + '/' + audio_file, ID3=EasyID3)
                # we need to use index 0, because the result is list
                song = Song(
                    mp3['title'][0],
                    mp3['artist'][0],
                    mp3['album'][0],
                    to_hour_str(mp3.info.length))
                playlist.add_song(song)
        return playlist

    @staticmethod
    def check_path(path):
        if type(path) is not str:
            raise TypeError("Type of music_path must be string.")
        if not(os.path.isdir(path)):
            raise ValueError("No such directory.")
        return True
