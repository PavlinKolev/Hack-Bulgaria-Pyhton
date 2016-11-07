import unittest
from game_of_life import Game_Of_Life


class Test_Game(unittest.TestCase):
    def setUp(self):
        self.live_cells = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [1, 3], [2, 0], [2, 1], [3, 1]]
        self.game = Game_Of_Life(4, self.live_cells)

    def test_create_empty_matrix(self):
        dead = self.game.dead_symbol
        matrix = [[dead, dead, dead, dead], [dead, dead, dead, dead],
        [dead, dead, dead, dead], [dead, dead, dead, dead]]
        self.assertEqual(self.game._create_empty_matrix(), matrix)

    def test_is_in_matrix(self):
        self.assertTrue(self.game._is_in_matrix([0, 0]))
        self.assertTrue(self.game._is_in_matrix([3, 3]))
        self.assertFalse(self.game._is_in_matrix([-1, 2]))

    def test_is_alive(self):
        dead = self.game.dead_symbol
        live = self.game.live_symbol
        matrix = [[live, dead, dead, dead], [dead, live, dead, dead],
        [dead, live, dead, dead], [live, dead, dead, dead]]
        self.assertTrue(self.game._is_alive([0, 0], matrix))
        self.assertFalse(self.game._is_alive([0, 1], matrix))

    def test_step_for_live(self):
        dead = self.game.dead_symbol
        live = self.game.live_symbol
        matrix = [[live, dead, dead, dead], [dead, live, dead, dead],
        [dead, live, dead, dead], [live, dead, dead, dead]]
        self.game._step_for_live([0, 0], matrix)
        self.assertFalse(self.game._is_alive([0, 0], matrix))

    def test_step_for_dead(self):
        dead = self.game.dead_symbol
        live = self.game.live_symbol
        matrix = [[live, dead, live, dead], [dead, live, dead, dead],
        [dead, live, dead, dead], [live, dead, dead, dead]]
        self.game._step_for_dead([0, 1], matrix)
        self.assertTrue(self.game._is_alive([0, 1], matrix))

    def test_is_game_over(self):
        self.assertTrue(self.game._is_game_over(self.live_cells))
        self.assertFalse(self.game._is_game_over([[1, 1], [2, 2]]))


if __name__ == '__main__':
    unittest.main()
