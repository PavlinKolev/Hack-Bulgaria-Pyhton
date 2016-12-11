import unittest
from song import Song
from hour import Hour


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Alone", "Alan Walker", "Alan Walker", "02:43")
        self.song_2 = Song("Cheap Thrills", "Sia", "This Is Acting", "03:31")

    def test_str(self):
        self.assertEqual(str(self.song_1), "Alan Walker - Alone from \"Alan Walker\" - 02:43")
        self.assertEqual(str(self.song_2), "Sia - Cheap Thrills from \"This Is Acting\" - 03:31")

    def test_eq(self):
        self.assertEqual(self.song_1, Song("Alone", "Alan Walker", "Alan Walker", "02:43"))
        self.assertEqual(self.song_2, Song("Cheap Thrills", "Sia", "This Is Acting", "03:31"))
        self.assertNotEqual(self.song_1, self.song_2)

    def test_hash(self):
        self.assertEqual(hash(self.song_1), hash(Song("Alone", "Alan Walker", "Alan Walker", "02:43")))
        self.assertEqual(hash(self.song_2), hash(Song("Cheap Thrills", "Sia", "This Is Acting", "03:31")))
        self.assertNotEqual(hash(self.song_1), hash(self.song_2))

    def test_length(self):
        self.assertEqual(self.song_1.length(), "02:43")
        self.assertEqual(self.song_2.length(), "03:31")

    def test_length_hours(self):
        self.assertEqual(self.song_1.length(hours=True), 0)
        self.assertEqual(self.song_2.length(hours=True), 0)

    def test_length_minutes(self):
        self.assertEqual(self.song_1.length(minutes=True), 2)
        self.assertEqual(self.song_2.length(minutes=True), 3)

    def test_length_seconds(self):
        self.assertEqual(self.song_1.length(seconds=True), 163)
        self.assertEqual(self.song_2.length(seconds=True), 211)

    def test_get_title(self):
        self.assertEqual(self.song_1.get_title(), "Alone")
        self.assertEqual(self.song_2.get_title(), "Cheap Thrills")

    def test_get_artist(self):
        self.assertEqual(self.song_1.get_artist(), "Alan Walker")
        self.assertEqual(self.song_2.get_artist(), "Sia")

    def test_get_album(self):
        self.assertEqual(self.song_1.get_album(), "Alan Walker")
        self.assertEqual(self.song_2.get_album(), "This Is Acting")

    def test_get_length(self):
        self.assertEqual(self.song_1.get_length(), Hour("02:43"))
        self.assertEqual(self.song_2.get_length(), Hour("03:31"))


if __name__ == '__main__':
    unittest.main()
