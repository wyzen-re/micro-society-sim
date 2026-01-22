import random
from agent import Agent

class Society:
    def __init__(self, population_size=20):
        self.agents = [Agent(i) for i in range(population_size)]
        self.groups = {}

    def form_groups(self):
        """Agents form groups based on loyalty"""
        self.groups = {}
        for agent in self.agents:
            if agent.group is None or random.random() > agent.loyalty:
                agent.group = random.randint(1, 3)

            self.groups.setdefault(agent.group, []).append(agent)

    def interactions(self):
        """Random interactions between agents"""
        for _ in range(len(self.agents) * 2):
            a, b = random.sample(self.agents, 2)
            a.interact(b)

    def average_cooperation(self):
        return sum(a.cooperation for a in self.agents) / len(self.agents)

    def summary(self, generation):
        print(
            f"Gen {generation:02d} | "
            f"Agents: {len(self.agents)} | "
            f"Groups: {len(self.groups)} | "
            f"Avg cooperation: {self.average_cooperation():.2f}"
        )
