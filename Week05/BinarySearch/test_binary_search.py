import unittest
from bin_search import binary_search, find_turning_point


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.sorted_array = [1, 2, 3, 4, 5]
        self.start = 0
        self.end = len(self.sorted_array) - 1

    def test_left_end(self):
        index = binary_search(self.sorted_array, self.start, self.end, 1)
        self.assertEqual(index, 0)

    def test_right_end(self):
        index = binary_search(self.sorted_array, self.start, self.end, 5)
        self.assertEqual(index, 4)

    def test_regular(self):
        index = binary_search(self.sorted_array, self.start, self.end, 2)
        self.assertEqual(index, 1)

    def test_not_fount(self):
        self.assertFalse(binary_search(self.sorted_array, self.start, self.end, 100))


class TestTurningPoint(unittest.TestCase):
    def test_regular_1(self):
        array = [1, 3, 7, 9, 10, 4, 2]
        index = find_turning_point(array, 0, len(array))
        self.assertEqual(index, 5)

    def test_regular_2(self):
        array = [1, 6, 4, 3, 2]
        index = find_turning_point(array, 0, len(array))
        self.assertEqual(index, 2)

    def test_second_number_turning(self):
        array = [6, 1, 4, 3, 2]
        index = find_turning_point(array, 0, len(array))
        self.assertEqual(index, 1)

    def test_find_first_turning(self):
        array = [12, 6, 7, 8, 2, 1]
        index = find_turning_point(array, 0, len(array))
        self.assertEqual(index, 1)

    def test_last_number_is_turning(self):
        array = [5, 6, 7, 8, 2]
        index = find_turning_point(array, 0, len(array))
        self.assertEqual(index, 4)

    def test_no_turning_point(self):
        array = [5, 6, 7, 8, 9]
        self.assertFalse(find_turning_point(array, 0, len(array)))


if __name__ == '__main__':
    unittest.main()
