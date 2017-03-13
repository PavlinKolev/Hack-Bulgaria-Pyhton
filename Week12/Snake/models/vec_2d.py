class Vec2D:
    def __init__(self, x, y):
        if (not type(x) is int) or (not type(y) is int):
            raise ValueError("Error type for Vec2D.")
        self.x = x
        self.y = y

    def get_x_y(self):
        return (self.x, self.y)

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2D(self.x * other.x, self.y * other.y)

    def __neg__(self):
        return Vec2D(-self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()
