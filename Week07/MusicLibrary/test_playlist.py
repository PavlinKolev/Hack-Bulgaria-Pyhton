import unittest
import json
from playlist import Playlist
from song import Song


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.playlist = Playlist("2016", repeat=False, shuffle=False)

    def test_eq(self):
        playlist_2 = Playlist("2016", repeat=False, shuffle=False)
        self.assertEqual(self.playlist, playlist_2)
        song_1 = Song("Cheap Thrills", "Sia", "This Is Acting", "03:31")
        song_2 = Song("Never Give Up", "Sia", "This Is Acting", "03:42")
        song_3 = Song("Alone", "Alan Walker", "Alan Walker", "02:43")
        self.playlist.add_songs([song_1, song_2, song_3])
        playlist_2.add_songs([song_1, song_2, song_3])
        self.assertEqual(self.playlist, playlist_2)

    def test_change_repeat(self):
        self.playlist.change_repeat(True)
        self.assertTrue(self.playlist.repeat)
        self.playlist.change_repeat(False)
        self.assertFalse(self.playlist.repeat)

    def test_change_shuffle(self):
        self.playlist.change_shuffle(True)
        self.assertTrue(self.playlist.shuffle)
        self.playlist.change_shuffle(False)
        self.assertFalse(self.playlist.shuffle)

    def test_save(self):
        song_1 = Song("Cheap Thrills", "Sia", "This Is Acting", "03:31")
        song_2 = Song("Never Give Up", "Sia", "This Is Acting", "03:42")
        song_3 = Song("Alone", "Alan Walker", "Alan Walker", "02:43")
        self.playlist.add_songs([song_1, song_2, song_3])
        self.playlist.save()
        f = open(Playlist.DEFAULT_FOLDER + "2016.json", 'r')
        data = json.load(f)
        f.close()
        expect = {"name": "2016", "repeat": False, "shuffle": False,\
            "songs": [{"title": "Cheap Thrills", "artist": "Sia", "album": "This Is Acting", "length": "03:31" },\
                    {"title": "Never Give Up", "artist": "Sia", "album": "This Is Acting", "length": "03:42"},\
                    {"title": "Alone", "artist": "Alan Walker", "album": "Alan Walker", "length": "02:43"}]}
        self.assertEqual(data, expect)

    def test_load(self):
        song_1 = Song("Cheap Thrills", "Sia", "This Is Acting", "03:31")
        song_2 = Song("Never Give Up", "Sia", "This Is Acting", "03:42")
        song_3 = Song("Alone", "Alan Walker", "Alan Walker", "02:43")
        p_list = Playlist("New playlist", repeat=True, shuffle=True)
        p_list.add_songs([song_1, song_2, song_3])
        p_list.save()
        p = Playlist.load("New-playlist.json")
        self.assertEqual(p, p_list)


if __name__ == '__main__':
    unittest.main()
