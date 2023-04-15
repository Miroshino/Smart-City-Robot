# Agent Class
class Agent:
    # Constructor method
    def __init__(self, battery: int = 10, points: int = 0, mission: str = "Delivery", position = (0, 0)):
        self.battery = battery
        self.points = points
        self.mission = mission
        self.position = position

        self.target_position = None

    # Getters
    def get_battery(self): return self.battery
    def get_points(self): return self.points
    def get_mission(self): return self.mission
    def get_position(self): return self.position
    def get_target_position(self): return self.target_position

    # Setters
    def set_battery(self, battery): self.battery = battery
    def set_points(self, points): self.points = points
    def set_mission(self, mission): self.mission = mission
    def set_position(self, position): self.position = position
    def set_target_position(self, target_position): self.target_position = target_position
