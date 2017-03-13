from models.python_models.python import Python
from models.python_models.python_head import PythonHead
from models.python_models.python_part import PythonPart
from models.world_objects import WorldObject, Food, BlackHole, Wall
from settings import MIN_WORLD_SIZE
from models.cell import Cell
from models.vec_2d import Vec2D
from Snake.helpers import gen_random_pair, gen_next_coords
from Snake.inputs import get
from Snake.exceptions import DeathError, DirectionError, WinError, InputError


class GameWorld:
    def __init__(self, size, content=None):
        self.__set_size(size)
        self.__set_matrix()
        self.snake = None
        self.snake_coords = []
        self.content = []
        self.foods = 0
        if content:
            self.add_content(content)

    def set_snake(self, snake):
        self.__set_snake_in_matrix(snake)
        self.snake = snake

    def run(self):
        while True:
            try:
                next_dir = get()
            except InputError:
                pass
            else:
                if next_dir != (-self.snake.direction):
                    try:
                        self.move(next_dir)
                    except IndexError:
                        print("Game Over! Out of the game world...")
                        return
                    except DeathError:
                        print("Game Over! You died...")
                        return
                    except WinError:
                        print("You won!!!")
                        return
                    else:
                        print(self)

    def move(self, next_dir):
        # import ipdb; ipdb.set_trace()
        new_coor = self.snake.coords + next_dir
        self.__validate_point(new_coor.y, new_coor.x)
        new_cell = self.matrix[new_coor.y][new_coor.x]
        if not new_cell.is_empty():
            if isinstance(new_cell.content, BlackHole):
                raise DeathError
            elif isinstance(new_cell.content, Wall):
                raise DeathError
            elif isinstance(new_cell.content, PythonPart):
                raise DeathError
            elif isinstance(new_cell.content, Food):
                # import ipdb; ipdb.set_trace()
                self.snake.score += new_cell.content.energy
                self.foods -= 1
                if self.foods == 0:
                    raise WinError
                self.snake.tail.append(PythonPart())
                self.snake_coords.append("Dummy")
        freed_cell = self.snake_coords.pop()
        if type(freed_cell) is Vec2D:
            self.matrix[freed_cell.y][freed_cell.x] = Cell()
        self.matrix[new_coor.y][new_coor.x] = Cell(PythonHead())
        self.matrix[self.snake_coords[0].y][self.snake_coords[0].x] = Cell(PythonPart())
        self.snake_coords = [new_coor] + self.snake_coords
        self.snake.coords = new_coor
        self.snake.direction = next_dir

    def __set_snake_in_matrix(self, snake):
        # import ipdb; ipdb.set_trace()
        temp_point = snake.coords
        for snake_part in [snake.head] + snake.tail:
            self.__validate_point(temp_point.y, temp_point.x)
            if not self.matrix[temp_point.y][temp_point.x].is_empty():
                self.__rearange_cells(temp_point.y, temp_point.x)
            self.matrix[temp_point.y][temp_point.x] = Cell(snake_part)
            self.snake_coords.append(temp_point)
            temp_point = gen_next_coords(temp_point, snake.direction)

    def __rearange_cells(self, y, x):
        for neighbor in DIRECTIONS:
            if self.matrix[neighbor.y][neighbor.x].is_empty():
                temp = self.matrix[neighbor.y][neighbor.x]
                self.matrix[neighbor.y][neighbor.x] = self.matrix[y][x]
                self.matrix[y][x] = temp
                return
        raise ValueError("Sorry, no free cell for snake python.")

    def __validate_point(self, x, y):
        if x < 0 or x >= self.size:
            raise IndexError("Index out of range")
        if y < 0 or y >= self.size:
            raise IndexError("Index out of range")

    def __set_matrix(self):
        self.matrix = [[Cell(x=i, y=j) for i in range(self.size)] for j in range(self.size)]

    def add_content(self, content):
        if isinstance(content, Cell):
            self.matrix[content.coords.x][content.coords.y] = content
            self.content.append(content)
            if isinstance(content.content, Food):
                self.foods += 1
            return
        self.__validate_content(content)
        gen = gen_random_pair(0, self.size - 1)
        for c in content:
            if c.has_coords():
                x, y = c.coords.get_x_y()
            else:
                x, y = next(gen)
                while not self.matrix[x][y].is_empty():
                    x, y = next(gen)
            self.matrix[x][y] = c
            self.content.append(c)
            if isinstance(c.content, Food):
                self.foods += 1

    def __set_size(self, size):
        if type(size) is not int:
            raise TypeError("Wrong type for world size")
        if size < MIN_WORLD_SIZE:
            raise ValueError("Too small size for world size")
        self.size = size

    def __validate_content(self, contents):
        if type(contents) is not list:
            raise TypeError("Wrong type for contents")
        if len(contents) >= (self.size**2) - self.size:
            raise ValueError("Too much contents for this world.")
        for c in contents:
            if not isinstance(c, Cell):
                raise TypeError("Wrong type for contents")

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.matrix[index]

    def __str__(self):
        result = ""
        for row in self.matrix:
            result += ''.join(map(str, row)) + '\n'
        return result

    def __repr__(self):
        return self.__str__()



def main():
    game = GameWorld(15)
    print(game)


if __name__ == '__main__':
    main()
