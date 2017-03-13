from models.world_objects import WorldObject, EmptyCell
from models.vec_2d import Vec2D


class Cell:
    def __init__(self, content=EmptyCell(), x=None, y=None):
        if not isinstance(content, WorldObject):
            raise ValueError("Incorect content!")
        self.content = content
        self.coords = None
        if x is not None and y is not None:
            self.coords = Vec2D(x, y)

    def has_coords(self):
        return bool(self.coords)

    def is_empty(self):
        return type(self.content) is EmptyCell

    def __str__(self):
        return str(self.content)

    def __repr__(self):
        return self.__str__()
