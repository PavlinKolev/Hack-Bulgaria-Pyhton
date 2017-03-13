from models.game_world import GameWorld
from models.world_objects import EmptyCell, Food, BlackHole, Wall
from models.cell import Cell
from models.python_models.python import Python
from models.vec_2d import Vec2D


def main():
    game = GameWorld(15)
    p = Python(game, Vec2D(10, 10), 3, Python.LEFT)

    wall1 = Cell(Wall(), 2, 7)
    wall2 = Cell(Wall(), 3, 7)
    wall3 = Cell(Wall(), 4, 7)
    game.add_content([wall1, wall2, wall3])

    cell1 = Cell(Food('banana', energy=3), 4, 0)
    cell2 = Cell(Food('mouse', energy=3), 0, 0)
    cell3 = Cell(Food('chick', energy=3), 1, 1)
    cell4 = Cell(Food('rabbit', energy=3), 4, 3)
    game.add_content(cell1)
    game.add_content(cell2)
    game.add_content(cell3)
    game.add_content(cell4)
    print(game)
    game.run()


if __name__ == '__main__':
    main()
