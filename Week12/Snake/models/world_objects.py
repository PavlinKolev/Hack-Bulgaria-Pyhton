from settings import WALL_SYMBOL, BLACK_HOLE_SYMBOL, FOOD_SYMBOLS, FOOD_DEFAULT_SYMBOL, EMPTY_CELL_SYMBOL


class WorldObject:
    def __init__(self):
        self.symbol = EMPTY_CELL_SYMBOL

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.__str__()


class EmptyCell(WorldObject):
    pass


class Wall(WorldObject):
    def __init__(self):
        self.symbol = WALL_SYMBOL


class Food(WorldObject):
    def __init__(self, name, energy):
        self.__set_name_and_symbol(name)
        self.energy = energy

    def __set_name_and_symbol(self, name):
        self.name = name
        try:
            self.symbol = FOOD_SYMBOLS[name]
        except KeyError:
            self.symbol = FOOD_DEFAULT_SYMBOL


class BlackHole(WorldObject):
    def __init__(self):
        self.symbol = BLACK_HOLE_SYMBOL
