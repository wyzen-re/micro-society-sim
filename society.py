import random
from agent import Agent
from world import World
from collections import defaultdict

class Society:
    def __init__(self, population_size=20, world_size=10):
        self.agents = [Agent(i) for i in range(population_size)]
        self.world = World(world_size)
        self.groups = defaultdict(list)
        self.positions = {}

        for agent in self.agents:
            self.positions[agent.id] = (
                random.randint(0, world_size - 1),
                random.randint(0, world_size - 1)
            )

    def form_groups(self):
        self.groups.clear()
        for agent in self.agents:
            if agent.alive:
                gid = int(agent.cooperation * 3)
                agent.group = gid
                self.groups[gid].append(agent)

    def step(self):
        for agent in self.agents:
            if not agent.alive:
                continue

            pos = self.positions[agent.id]
            food = self.world.harvest(pos)
            agent.forage(food)
            agent.consume_food()

            # random movement
            x, y = pos
            self.positions[agent.id] = (
                max(0, min(self.world.size - 1, x + random.choice([-1, 0, 1]))),
                max(0, min(self.world.size - 1, y + random.choice([-1, 0, 1])))
            )

    def conflict(self):
        cell_groups = defaultdict(list)

        for agent in self.agents:
            if agent.alive:
                cell_groups[self.positions[agent.id]].append(agent)

        for cell, agents in cell_groups.items():
            groups = set(a.group for a in agents)
            if len(groups) > 1:
                winner = max(agents, key=lambda a: a.aggression)
                for a in agents:
                    if a != winner:
                        a.food -= 2
                        if a.food <= 0:
                            a.alive = False

    def summary(self):
        alive = sum(a.alive for a in self.agents)
        print(f"\nAlive agents: {alive}")
        for gid, members in self.groups.items():
            alive_members = sum(a.alive for a in members)
            print(f"Group {gid}: {alive_members} alive")
