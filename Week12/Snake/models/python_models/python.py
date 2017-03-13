from models.python_models.python_head import PythonHead
from models.python_models.python_part import PythonPart
from settings import MIN_PYTHON_SIZE
from models.vec_2d import Vec2D
from Snake.exceptions import DirectionError

DIRECTIONS = {
    'left': Vec2D(-1, 0),
    'right': Vec2D(1, 0),
    'down': Vec2D(0, 1),
    'up': Vec2D(0, -1)
}


class Python:
    LEFT = DIRECTIONS['left']
    RIGHT = DIRECTIONS['right']
    UP = DIRECTIONS['up']
    DOWN = DIRECTIONS['down']

    def __init__(self, world, coords, size, direction):
        # import ipdb; ipdb.set_trace()
        self.head = PythonHead()
        self.__set_coords(coords)
        self.__set_size(size)
        self.__set_direction(direction)
        self.tail = [PythonPart() for _ in range(self.size)]
        world.set_snake(self)
        self.score = 0

    def __set_coords(self, coords):
        if not type(coords) is Vec2D:
            raise ValueError("Wrong type for coords")
        self.coords = coords

    def __set_size(self, size):
        if not type(size) is int:
            raise TypeError("Wrong type for python size")
        if size < MIN_PYTHON_SIZE:
            raise ValueError("Too small size for python")
        self.size = size

    def __set_direction(self, direction):
        if direction not in DIRECTIONS.values():
            raise DirectionError("Wrong direction for Pyhton snake.")
        self.direction = direction
