# Agent Class
class Agent:
    # Constructor method
    def __init__(self, battery: int = 10, points: int = 0, mission: str = "Delivery", position = (0, 0), color: str = "blue"):
        self.battery = battery
        self.points = points
        self.mission = mission
        self.position = position
        self.color = color
        self.move_positions = []

        self.target_position = None

    # Getters
    def get_battery(self): return self.battery
    def get_points(self): return self.points
    def get_mission(self): return self.mission
    def get_position(self): return self.position
    def get_target_position(self): return self.target_position
    def get_color(self): return self.color
    def get_move_positions(self): return self.move_positions

    # Setters
    def set_battery(self, battery): self.battery = battery
    def set_points(self, points): self.points = points
    def set_mission(self, mission): self.mission = mission
    def set_position(self, position): self.position = position
    def set_target_position(self, target_position): self.target_position = target_position
    def set_color(self, color): self.color = color
    def set_move_positions(self, move_positions): self.move_positions = move_positions

    # Method(s)
    # Method: move
    # Purpose: Move the agent to positions in the list, one by one
    def move(self, positions: list):
        pass
