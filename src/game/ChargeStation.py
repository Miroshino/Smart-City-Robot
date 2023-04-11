# Charge Station Class
class ChargeStation:
    # Constructor method
    def __init__(self, isOccupied: bool = False, position = (0, 0)):
        self.isOccupied = isOccupied
        self.position = position

    # Getters
    def get_isOccupied(self): return self.isOccupied
    def get_position(self): return self.position

    # Setters
    def set_isOccupied(self, isOccupied): self.isOccupied = isOccupied
    def set_position(self, position): self.position = position
    