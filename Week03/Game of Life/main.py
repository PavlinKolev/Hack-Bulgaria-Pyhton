from sys import argv
from game_of_life import Game_Of_Life
from parser import Parser


def start_game():
    file_info = argv[1]
    info = Parser.parse_start_info(file_info)

    matrix_size = info[0]
    live_cells = info[1]

    game = Game_Of_Life(matrix_size, live_cells)
    game.run_game()


if __name__ == "__main__":
    start_game()
