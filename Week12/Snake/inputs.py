import sys
import tty
import termios
from models.python_models.python import DIRECTIONS
from Snake.exceptions import InputError


class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def get():
    inkey = _Getch()
    k = inkey()
    if k == '\x1b[A':
        return DIRECTIONS["up"]
    elif k == '\x1b[B':
        return DIRECTIONS["down"]
    elif k == '\x1b[C':
        return DIRECTIONS["right"]
    elif k == '\x1b[D':
        return DIRECTIONS["left"]
    else:
        raise InputError("Not an arrow key!")
