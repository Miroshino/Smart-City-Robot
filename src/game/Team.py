# Import(s)
from game import Agent


# Team Class
class Team:
    # Constructor method
    def __init__(self, color: str = "blue", points: int = 0, agents=None):
        # Attribute(s)
        if agents is None:
            agents = []
        self.color = color
        self.points = points
        self.agents = agents

    # Getters
    def get_color(self): return self.color
    def get_points(self): return self.points
    def get_agents(self): return self.agents

    # Setters
    def set_color(self, color): self.color = color
    def set_points(self, points): self.points = points
    def set_agents(self, agents): self.agents = agents

    # Method(s)
    # Method: add_agent
    # Purpose: Add an agent to the team
    def add_agent(self, agent: Agent):
        self.agents.append(agent)

    # Method: remove_agent
    # Purpose: Remove an agent from the team
    def remove_agent(self, agent: Agent):
        self.agents.remove(agent)

    # Method: add_points
    # Purpose: Add points to the team
    def add_points(self, points: int):
        self.points = self.points + points

    # Method: remove_points
    # Purpose: Remove points from the team
    def remove_points(self, points: int):
        self.points = self.points - points
