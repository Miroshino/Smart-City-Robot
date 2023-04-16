# Import(s)
import map.Tiles as Tiles
import algorithm.Math as Math
import game.Agent as Agent
import map.Session as Session
from queue import PriorityQueue


# AStar Class
class AStar:
    # Constructor method
    def __init__(self, tiles: Tiles, agent: Agent, session: Session):
        # Attribute(s)
        self.agent = agent
        self.session = session
        self.start_position = agent.get_position()
        self.end_position = None
        self.tiles = tiles
        self.buttons = self.tiles.get_buttons()

        # Variable(s)
        self.math = Math.Math()

    # Getters
    def get_agent(self): return self.agent
    def get_session(self): return self.session
    def get_start_position(self): return self.start_position
    def get_end_position(self): return self.end_position
    def get_buttons(self): return self.buttons

    # Setters
    def set_agent(self, agent): self.agent = agent
    def set_session(self, session): self.session = session
    def set_start_position(self, start_position): self.start_position = start_position
    def set_end_position(self, end_position): self.end_position = end_position
    def set_buttons(self, buttons): self.buttons = buttons

    # Method(s)
    # Method: set_end_point
    # Purpose: Set the end point of the path based on the agent's mission
    def set_end_point(self):
        # Variable(s)
        mission = self.agent.get_mission()

        # Get the points based on the mission
        if mission == "storage":
            points = self.get_session().get_storage_points()
        elif mission == "charging":
            points = self.get_session().get_charge_stations_points()
            self.agent.set_battery(100)
        elif mission == "delivery":
            points = self.get_session().get_delivery_points()
        else:
            return 2, 2  # Default position if mission is invalid

        # Set the end position to the closest point
        distances = [int(Math.Math().get_distance(self.get_start_position(), p.get_position())) for p in points]
        self.set_end_position(points[distances.index(min(distances))].get_position())

    # Method: find_path
    # Purpose: Find the path from the start position to the end position
    def find_path(self):
        # Find and set the end position
        self.set_end_point()

        # Variable(s)
        open_set = PriorityQueue()
        open_set.put((0, self.start_position))
        came_from = {}
        g_score = {self.start_position: 0}  # Distance from start_position to current_pos
        f_score = {self.start_position: self.math.heuristic(self.start_position, self.end_position)}  # Distance from start_position to end_position
        allowed_colors = ["white", "green", "blue", "red"]

        # While open_set isn't empty
        while not open_set.empty():
            # Change current_pos
            current_pos = open_set.get()[1]  # Get the position of the button

            # Check if current_pos is 1 tile away from the end_position
            if abs(current_pos[0] - self.end_position[0]) + abs(current_pos[1] - self.end_position[1]) == 1:
                return self.reconstruct_path(came_from, current_pos)[::-1]

            for neighbor_position in self.get_neighbors(current_pos):
                neighbor_color = self.tiles.get_button(neighbor_position[0], neighbor_position[1]).cget("bg")  # Get the neighbor color

                # Check if the neighbor color is allowed
                if neighbor_color not in allowed_colors:
                    continue

                # Calculate tentative_g_score
                tentative_g_score = g_score[current_pos] + 1  # Calculate tentative_g_score

                # Check if tentative_g_score is better than g_score
                if neighbor_position not in g_score or tentative_g_score < g_score[neighbor_position]:
                    came_from[neighbor_position] = current_pos  # Change came_from
                    g_score[neighbor_position] = tentative_g_score  # Calculate g_score
                    f_score[neighbor_position] = tentative_g_score + self.math.heuristic(neighbor_position, self.end_position)  # Calculate f_score
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
