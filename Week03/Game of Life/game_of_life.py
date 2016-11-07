import time
import os

class Game_Of_Life:
    #  Public
    def __init__(self, matrix_size, live_cells):
        self.matrix_size = matrix_size
        self.live_cells = live_cells  # list from the live cells
        self.dead_symbol = '☠'
        self.live_symbol = '☻'

    #  Public
    def run_game(self):
        while True:
            matrix = self._create_empty_matrix()
            self._set_live_cells(matrix)

            os.system('clear')
            self._print_matrix(matrix)
            time.sleep(0.5)

            new_live_cells = self._reload_live_cells(matrix)
            if self._is_game_over(new_live_cells):
                break

            self.live_cells = new_live_cells

    #  Private
    def _create_empty_matrix(self):
        matrix = []
        for index1 in range(self.matrix_size):
            line = []
            for index2 in range(self.matrix_size):
                line.append(self.dead_symbol)
            matrix.append(line)
        return matrix

    #  Private
    def _print_matrix(self, matrix):
        for index in range(self.matrix_size):
            line = " ".join(matrix[index])
            print(line)

    #  Private
    def _set_live_cells(self, matrix):
        for cell in self.live_cells:
            matrix[cell[0]][cell[1]] = self.live_symbol

    #  Private
    def _get_neighbor(self, cell, cell_neigh):
        list_neighs = [[-1, -1], [-1, 0], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        coorX = cell[0] + list_neighs[cell_neigh][0]
        coorY = cell[1] + list_neighs[cell_neigh][1]
        return [coorX, coorY]

    #  Private
    def _is_in_matrix(self, cell):
        if cell[0] < 0 or cell[0] >= self.matrix_size:
            return False
        if cell[1] < 0 or cell[1] >= self.matrix_size:
            return False
        return True

    #  Private
    def _is_alive(self, cell, matrix):
        if matrix[cell[0]][cell[1]] == self.live_symbol:
            return True
        return False

    #  Private
    def _step_for_live(self, cell, matrix):
        count_live_neighs = 0
        for index in range(8):
            neigh = self._get_neighbor(cell, index)
            if self._is_in_matrix(neigh):
                if self._is_alive(neigh, matrix):
                    count_live_neighs += 1
        if count_live_neighs != 2 and count_live_neighs != 3:
            matrix[cell[0]][cell[1]] = self.dead_symbol

    #  Private
    def _step_for_dead(self, cell, matrix):
        count_live_neighs = 0
        for index in range(8):
            neigh = self._get_neighbor(cell, index)
            if self._is_in_matrix(neigh):
                if self._is_alive(neigh, matrix):
                    count_live_neighs += 1
        if count_live_neighs == 3:
            matrix[cell[0]][cell[1]] = self.live_symbol

    #  Private
    def _reload_live_cells(self, matrix):
        new_live_cells = []

        for index1 in range(self.matrix_size):
            for index2 in range(self.matrix_size):
                cell = [index1, index2]

                if self._is_alive(cell, matrix):
                    self._step_for_live(cell, matrix)
                else:
                    self._step_for_dead(cell, matrix)

                if self._is_alive(cell, matrix):
                    new_live_cells.append(cell)
        return new_live_cells

    #  Private
    def _is_game_over(self, new_live_cells):
        previous_live_cells = set(map(tuple, self.live_cells))
        current_live_cells = set(map(tuple, new_live_cells))
        if previous_live_cells == current_live_cells:
            return True
        else:
            return False
