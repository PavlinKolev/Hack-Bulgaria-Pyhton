import unittest
from song_list import SongList
from song import Song


class TestSongList(unittest.TestCase):
    def setUp(self):
        self.song_list = SongList()

    def test_eq(self):
        song_list_2 = SongList()
        song_1 = Song("Cheap Thrills", "Sia", "This Is Acting", "03:31")
        song_2 = Song("Never Give Up", "Sia", "This Is Acting", "03:42")
        song_3 = Song("Alone", "Alan Walker", "Alan Walker", "02:43")
        self.song_list.add_songs([song_1, song_2, song_3])
        song_list_2.add_songs([song_1, song_3])
        self.song_list.remove_song(song_2)
        self.assertEqual(self.song_list, song_list_2)

    def test_add_song(self):
        song = Song("Cheap Thrills", "Sia", "This Is Acting", "03:31")
        self.song_list.add_song(song)
        self.assertIn(song, self.song_list.songs)
        self.assertEqual(self.song_list.artists_hist["Sia"], 1)

    def test_remove_song(self):
        song = Song("Cheap Thrills", "Sia", "This Is Acting", "03:31")
        self.song_list.add_song(song)
        self.song_list.remove_song(song)
        self.assertNotIn(song, self.song_list.songs)
        self.assertEqual(self.song_list.artists_hist["Sia"], 0)

    def test_add_songs(self):
        song_1 = Song("Cheap Thrills", "Sia", "This Is Acting", "03:31")
        song_2 = Song("Never Give Up", "Sia", "This Is Acting", "03:42")
        song_3 = Song("Alone", "Alan Walker", "Alan Walker", "02:43")
        s_list = [song_1, song_2, song_3]
        self.song_list.add_songs(s_list)
        self.assertIn(song_1, self.song_list.songs)
        self.assertIn(song_2, self.song_list.songs)
        self.assertIn(song_3, self.song_list.songs)
        self.assertEqual(self.song_list.artists_hist["Sia"], 2)
        self.assertEqual(self.song_list.artists_hist["Alan Walker"], 1)

    def test_total_length(self):
        song_1 = Song("Cheap Thrills", "Sia", "This Is Acting", "03:31")
        song_2 = Song("Never Give Up", "Sia", "This Is Acting", "03:42")
        song_3 = Song("Alone", "Alan Walker", "Alan Walker", "02:43")
        s_list = [song_1, song_2, song_3]
        self.song_list.add_songs(s_list)
        self.assertEqual(self.song_list.total_length(), "09:56")

    def test_artists(self):
        song_1 = Song("Cheap Thrills", "Sia", "This Is Acting", "03:31")
        song_2 = Song("Never Give Up", "Sia", "This Is Acting", "03:42")
        song_3 = Song("Alone", "Alan Walker", "Alan Walker", "02:43")
        s_list = [song_1, song_2, song_3]
        self.song_list.add_songs(s_list)
        self.assertEqual(self.song_list.artists(), {"Alan Walker": 1, "Sia": 2})

    def test_next_song(self):
        song_1 = Song("Cheap Thrills", "Sia", "This Is Acting", "03:31")
        song_2 = Song("Never Give Up", "Sia", "This Is Acting", "03:42")
        song_3 = Song("Alone", "Alan Walker", "Alan Walker", "02:43")
        s_list = [song_1, song_2, song_3]
        self.song_list.add_songs(s_list)
        self.assertEqual(self.song_list.next_song(repeat=False, shuffle=False), song_1)
        self.assertEqual(self.song_list.next_song(repeat=False, shuffle=False), song_2)
        self.assertEqual(self.song_list.next_song(repeat=False, shuffle=False), song_3)
        self.assertFalse(self.song_list.next_song(repeat=False, shuffle=False))
        self.assertEqual(self.song_list.next_song(repeat=True, shuffle=False), song_1)

    def test_get_json_songs(self):
        song_1 = Song("Cheap Thrills", "Sia", "This Is Acting", "03:31")
        song_2 = Song("Never Give Up", "Sia", "This Is Acting", "03:42")
        song_3 = Song("Alone", "Alan Walker", "Alan Walker", "02:43")
        s_list = [song_1, song_2, song_3]
        self.song_list.add_songs(s_list)
        expect = [{"title": "Cheap Thrills", "artist": "Sia", "album": "This Is Acting", "length": "03:31" },\
                {"title": "Never Give Up", "artist": "Sia", "album": "This Is Acting", "length": "03:42"},\
                {"title": "Alone", "artist": "Alan Walker", "album": "Alan Walker", "length": "02:43"}]
        self.assertEqual(self.song_list.get_json_songs(), expect)


if __name__ == '__main__':
    unittest.main()
