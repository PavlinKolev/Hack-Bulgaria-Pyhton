from models.world_objects import WorldObject
from settings import PYTHON_PART_SYMBOL


class PythonPart(WorldObject):
    def __init__(self):
        self.symbol = PYTHON_PART_SYMBOL
