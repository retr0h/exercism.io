NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.x = x
        self.y = y
        self.bearing = bearing

    @property
    def coordinates(self):
        return self.x, self.y

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
        for instruction in instructions:
            if instruction == 'L':
                self.turn_left()
            elif instruction == 'R':
                self.turn_right()
            elif instruction == 'A':
                self.advance()
