# Point Class
class Point:
    # Constructor method
    def __init__(self, point_type: str = "spawn_point", position = (0, 0), color: str = "red"):
        self.point_type = point_type
        self.position = position
        self.color = color

    # Getters
    def get_point_type(self): return self.point_type
    def get_position(self): return self.position
    def get_color(self): return self.color

    # Setters
    def set_point_type(self, point_type): self.point_type = point_type
    def set_position(self, position): self.position = position
    def set_color(self, color): self.color = color
