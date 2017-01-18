import unittest
from generators import chain, compress, cycle


class TestGenerators(unittest.TestCase):
    def test_chain(self):
        res = list(chain(range(0, 4), range(4, 8)))
        expected = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(res, expected)

    def test_compress(self):
        res = list(compress(["Ivo", "Rado", "Panda"], [False, False, True]))
        expected = ["Panda"]
        self.assertEqual(res, expected)

    def test_cycle(self):
        res = []
        i = 0
        for elem in cycle(range(10)):
            if i == 17:
                break
            res.append(elem)
            i += 1
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
        self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()
