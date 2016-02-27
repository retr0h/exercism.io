NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self._x = x
        self._y = y
        self._bearing = bearing

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def coordinates(self):
        return self.x, self.y

    @property
    def bearing(self):
        return self._bearing

    @bearing.setter
    def bearing(self, value):
        self._bearing = value

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def advance(self):
        if self.bearing == NORTH:
            self.y += 1
        elif self.bearing == EAST:
            self.x += 1
        elif self.bearing == SOUTH:
            self.y += -1
        elif self.bearing == WEST:
            self.x += -1

    def simulate(self, instructions):
        print list(instructions)
        for instruction in list(instructions):
            if instruction == 'L':
                self.turn_left()
            elif instruction == 'R':
                self.turn_right()
            elif instruction == 'A':
                self.advance()
