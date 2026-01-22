import random

class Tile:
    def __init__(self):
        self.food = random.randint(3, 7)
        self.owner = None  # group id

    def regenerate(self):
        self.food = min(self.food + 1, 10)


class World:
    def __init__(self, size=10):
        self.size = size
        self.grid = [[Tile() for _ in range(size)] for _ in range(size)]

    def step(self):
        for row in self.grid:
            for tile in row:
                tile.regenerate()

    def random_position(self):
        return random.randint(0, self.size - 1), random.randint(0, self.size - 1)
