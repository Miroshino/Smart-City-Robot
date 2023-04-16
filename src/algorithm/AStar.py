# Import(s)
import map.Tiles as Tiles
from queue import PriorityQueue


# AStar Class
class AStar:
    # Constructor method
    def __init__(self, tiles: Tiles, start_position: tuple, end_pos: tuple):
        # Attribute(s)
        self.start_position = start_position
        self.end_position = end_pos
        self.tiles = tiles
        self.buttons = self.tiles.get_buttons()

    # Getters
    def get_start_position(self): return self.start_position
    def get_end_position(self): return self.end_position
    def get_buttons(self): return self.buttons

    # Setters
    def set_start_position(self, start_position): self.start_position = start_position
    def set_end_position(self, end_position): self.end_position = end_position
    def set_buttons(self, buttons): self.buttons = buttons

    # Method(s)
    # Method: find_path
    # Purpose: Find the path from the start position to the end position
    def find_path(self):
        # Variable(s)
        open_set = PriorityQueue()
        open_set.put((0, self.start_position))
        came_from = {}
        g_score = {self.start_position: 0}  # Distance from start_position to current_pos
        f_score = {self.start_position: self.heuristic(self.start_position, self.end_position)}  # Distance from start_position to end_position

        # While open_set isn't empty
        while not open_set.empty():
            # Change current_pos
            current_pos = open_set.get()[1]  # Get the position of the button

            # Check if current_pos == end_position (if it's finished)
            if current_pos == self.end_position:
                return self.reconstruct_path(came_from, self.end_position)[::-1] # Reverse the path

            for neighbor_position in self.get_neighbors(current_pos):
                tentative_g_score = g_score[current_pos] + 1  # Calculate tentative_g_score

                if neighbor_position not in g_score or tentative_g_score < g_score[neighbor_position]:
                    came_from[neighbor_position] = current_pos  # Change came_from
                    g_score[neighbor_position] = tentative_g_score  # Calculate g_score
                    f_score[neighbor_position] = tentative_g_score + self.heuristic(neighbor_position, self.end_position)  # Calculate f_score
                    open_set.put((f_score[neighbor_position], neighbor_position))  # Add neighbor_position to open_set

        # Return nothing
        return None

    # Method: get_neighbors
    # Purpose: Get every neighbors based on the tuple position list of buttons
    def get_neighbors(self, current_pos):
        # Variable(s)
        neighbors = []

        # Loop to get every neighbors
        for button in self.buttons:
            # Get the button position
            button_pos = (button.grid_info()['row'], button.grid_info()['column'])

            # Check if the button is a neighbor
            if abs(button_pos[0] - current_pos[0]) + abs(button_pos[1] - current_pos[1]) == 1:
                neighbors.append(button_pos)

        # Return neighbors
        return neighbors

    # Method: heuristic
    # Purpose: Calculate the heuristic
    def heuristic(self, a_pos: tuple, b_pos: tuple):
        # Return the heuristic
        return abs(a_pos[0] - b_pos[0]) + abs(a_pos[1] - b_pos[1])

    # Method: reconstruct_path
    # Purpose: Reconstruct the path
    def reconstruct_path(self, came_from: dict, current_pos: tuple):
        # Variable(s)
        total_path = []

        # While current_pos is in came_from
        while current_pos in came_from:
            total_path.append(current_pos)  # Add current_pos to total_path
            current_pos = came_from[current_pos]  # Change current_pos

        total_path.append(self.start_position)  # Add start_position to total_path

        # Return the total path
        return total_path
