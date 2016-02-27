class Robot(object):
    def __init__(self, bearing=None, x=0, y=0):
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
        if self._bearing is None:
            self._bearing = NORTH
            return self._bearing
        return self._bearing

    @bearing.setter
    def bearing(self, value):
        self._bearing = value

    def turn_right(self):
        if self.bearing == NORTH:
            self.bearing = EAST
        elif self.bearing == EAST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = NORTH

    def turn_left(self):
        if self.bearing == NORTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = SOUTH
        elif self.bearing == SOUTH:
            self.bearing = EAST
        elif self.bearing == EAST:
            self.bearing = NORTH

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


class NORTH(object):

    pass


class EAST(object):

    pass


class SOUTH(object):

    pass


class WEST(object):

    pass
