from models.python_models.python_part import PythonPart
from settings import PYTHON_HEAD_SYMBOL


class PythonHead(PythonPart):
    def __init__(self):
        self.symbol = PYTHON_HEAD_SYMBOL
