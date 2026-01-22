import random

class Agent:
    def __init__(self, agent_id):
        self.id = agent_id
        self.group = None
        self.food = random.randint(5, 10)
        self.aggression = random.random()      # 0–1
        self.cooperation = random.random()     # 0–1
        self.alive = True

    def consume_food(self):
        self.food -= 1
        if self.food <= 0:
            self.alive = False

    def forage(self, amount):
        self.food += amount
