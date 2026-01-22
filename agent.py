import random

class Agent:
    def __init__(self, agent_id):
        self.id = agent_id
        
        # psychological traits (0–1)
        self.cooperation = random.uniform(0.2, 0.8)
        self.aggression = random.uniform(0.1, 0.6)
        self.loyalty = random.uniform(0.3, 0.9)
        
        self.group = None
        self.resources = random.randint(5, 10)

    def interact(self, other):
        """Simple social interaction"""
        if random.random() < self.cooperation:
            # cooperate → share resources
            shared = 1
            self.resources -= shared
            other.resources += shared
            return "cooperate"
        else:
            # conflict
            if self.aggression > other.aggression:
                self.resources += 1
                other.resources -= 1
                return "win"
            else:
                self.resources -= 1
                other.resources += 1
                return "lose"
