import random
from collections import defaultdict

class World:
    def __init__(self, size=10):
        self.size = size
        self.grid = {}
        self.control = defaultdict(list)  # cell -> group

        for x in range(size):
            for y in range(size):
                self.grid[(x, y)] = random.randint(1, 5)  # food per cell

    def harvest(self, position):
        food = self.grid[position]
        self.grid[position] = max(0, food - 1)
        return food

    def regenerate(self):
        for pos in self.grid:
            self.grid[pos] += random.choice([0, 1])
